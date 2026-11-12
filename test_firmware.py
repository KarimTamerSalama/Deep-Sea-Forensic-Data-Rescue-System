# Automated unit test for fail-safe solenoid actuation logic
SAFE_PRESSURE_LIMIT_HPA = 1050.0

def evaluate_solenoid_state(pressure_hpa):
    return 1 if pressure_hpa > SAFE_PRESSURE_LIMIT_HPA else 0

def run_tests():
    assert evaluate_solenoid_state(1013.25) == 0, "Should stay locked at normal sea-level pressure"
    assert evaluate_solenoid_state(1050.0) == 0, "Should stay locked at exact threshold"
    assert evaluate_solenoid_state(1100.5) == 1, "Should trigger release above safe pressure limit"
    print("All firmware logic tests passed successfully!")

if __name__ == "__main__":
    run_tests()
