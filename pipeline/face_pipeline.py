from deepface import DeepFace
import numpy as np
from sklearn.svm import SVC
import streamlit as st

from database.db import get_all_students


@st.cache_resource
def load_face_model():
    return True


def get_face_embeddings(image_np):

    try:

        embedding_objs = DeepFace.represent(
            img_path=image_np,
            model_name="Facenet",
            enforce_detection=False
        )

        encodings = []

        for obj in embedding_objs:
            encodings.append(np.array(obj["embedding"]))

        return encodings

    except Exception as e:
        st.error(f"Face embedding error: {e}")
        return []


@st.cache_resource
def get_trained_model():

    X = []
    y = []

    student_db = get_all_students()

    if not student_db:
        return None

    for student in student_db:

        embedding = student.get("face_embedding")

        if embedding:

            X.append(np.array(embedding))
            y.append(student.get("student_id"))

    if len(X) == 0:
        return None

    clf = SVC(
        kernel="linear",
        probability=True,
        class_weight="balanced"
    )

    try:
        clf.fit(X, y)

    except ValueError as e:
        st.error(f"Training error: {e}")
        return None

    return {
        "clf": clf,
        "X": X,
        "y": y
    }


def train_classifier():

    st.cache_resource.clear()

    model_data = get_trained_model()

    return bool(model_data)


def predict_attendance(class_image_np):

    encodings = get_face_embeddings(class_image_np)

    detected_student = {}

    model_data = get_trained_model()

    if not model_data:
        return detected_student, [], len(encodings)

    clf = model_data["clf"]
    X_train = model_data["X"]
    y_train = model_data["y"]

    all_students = sorted(list(set(y_train)))

    for encoding in encodings:

        if len(all_students) >= 2:

            predicted_id = int(
                clf.predict([encoding])[0]
            )

        else:

            predicted_id = int(all_students[0])

        student_embedding = X_train[
            y_train.index(predicted_id)
        ]

        best_match_score = np.linalg.norm(
            student_embedding - encoding
        )

        resemblance_threshold = 10

        if best_match_score <= resemblance_threshold:
            detected_student[predicted_id] = True

    return (
        detected_student,
        all_students,
        len(encodings)
    )