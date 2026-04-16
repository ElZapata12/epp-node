from ultralytics import YOLO
import cv2
import time

DEVICE_ID = "mac-dev-001"

model = YOLO("../yolo26n.pt")
cap = cv2.VideoCapture(0)

TIMEOUT = 10  # segundos

last_person_time = None
person_status = False


def parse_results(results):
    detections = []

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])

            if conf < 0.8:
                continue

            detections.append({
                "class": model.names[cls],
                "confidence": conf
            })

    return detections


def detect_person(detections):
    return any(d["class"] == "person" for d in detections)


def send(person):
    payload = {
        "device_id": DEVICE_ID,
        "timestamp": time.time(),
        "data": {
            "person": person
        }
    }

    print("\nEVENTO:")
    print(payload)


while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, verbose=False)
    detections = parse_results(results)

    current_time = time.time()
    person_detected = detect_person(detections)

    # Caso de persona detectada
    if person_detected:
        last_person_time = current_time

        if person_status is False:
            person_status = True
            print("Persona detectada")
            send(True)

    # caso de persona no detectada
    else:
        if last_person_time is not None:
            elapsed = current_time - last_person_time

            if elapsed >= TIMEOUT and person_status is True:
                person_status = False
                print("falta persona por mas de 10 segundos")
                send(False)

    annotated = results[0].plot()
    cv2.imshow("Person Detection", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
