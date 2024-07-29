import subprocess

def run_terraform_plan():
    try:
        result = subprocess.run(['terraform', 'plan', '-detailed-exitcode'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result
    except Exception as e:
        print(f"Error running terraform plan: {e}")
        return None

def check_drift(result):
    if result.returncode == 2:
        return True, result.stdout
    elif result.returncode == 0:
        return False, "No drift detected"
    else:
        return False, f"Error: {result.stderr}"

if __name__ == "__main__":
    result = run_terraform_plan()
    if result:
        drift_detected, message = check_drift(result)
        print(message)

        if drift_detected:
            exit(1)
