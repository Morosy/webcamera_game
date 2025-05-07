import cv2
import mediapipe as mp

# 初期化
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, refine_landmarks=False)

# カメラ起動 & 解像度 1280x720 (16:9)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # 反転処理
    frame = cv2.flip(frame, 1)

    # RGBに変換
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            h, w, _ = frame.shape

            # 鼻先のランドマークID = 1
            nose = face_landmarks.landmark[1]
            x, y = int(nose.x * w), int(nose.y * h)

            # 鼻の位置に赤い円を描画（座標表示なし）
            cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)

    cv2.imshow("Nose Tracking Only", frame)

    # Escキーで終了（Esc = 27）
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
