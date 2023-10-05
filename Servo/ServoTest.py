import time
import pi_servo_hat

TILT_SERVO = 0
PAN_SERVO = 1

# Create an instance of the Servo Phat
servos = pi_servo_hat.PiServoHat()
servos.restart()

try:
    while True:
        servos.move_servo_position(TILT_SERVO, 90)
        servos.move_servo_position(PAN_SERVO, 45)

        # Wait for 1 second
        time.sleep(1)

        servos.move_servo_position(TILT_SERVO, 80)
        servos.move_servo_position(PAN_SERVO, 135)

        # Wait for 1 second
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    # Ensure the PWM outputs are off before exiting
    servos.disable_servo(TILT_SERVO)
    servos.disable_servo(PAN_SERVO)
