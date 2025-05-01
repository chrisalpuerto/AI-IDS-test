from detector import classify_packet

features = [123, 6, 64, 1000, 500]
label = classify_packet(features)
print(f"Packet classified as: {label}")