from machine import Pin
import time

# Inisialisasi pin
IN1 = Pin(13, Pin.OUT)
IN2 = Pin(12, Pin.OUT)
IN3 = Pin(14, Pin.OUT)
IN4 = Pin(27, Pin.OUT)

# Urutan langkah full-step (putaran searah jarum jam)
step_sequence = [
    (1, 0, 1, 0),
    (0, 1, 1, 0),
    (0, 1, 0, 1),
    (1, 0, 0, 1)
]

def set_step(a, b, c, d):
    IN1.value(a)
    IN2.value(b)
    IN3.value(c)
    IN4.value(d)

while True:
    for step in step_sequence:
        set_step(*step)
        time.sleep(0.01)  # Semakin kecil, makin cepat