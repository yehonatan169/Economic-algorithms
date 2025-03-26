import cvxpy
import math

def compute_optimal_allocation(t):
    """
    מחשב את החלוקה האופטימלית בין עמי ותמי, עבור ערך נתון של t,
    באמצעות מקסום log(x) + log(1 - t*x) ב-cvxpy.
    """
    x = cvxpy.Variable()
    objective = cvxpy.Maximize(cvxpy.log(x) + cvxpy.log(1 - t * x))
    constraints = [x >= 0, x <= 1]
    prob = cvxpy.Problem(objective, constraints)
    prob.solve()

    x_val = float(x.value)
    value_ammi = x_val
    value_tami = float(t * (1 - x_val) + (1 - t))

    return {
        'status': prob.status,
        'ammi_value': value_ammi,
        'tami_value': value_tami
    }


def run_manual_tests():
    tests = [
        {"t": 0.25, "expected_ammi": 1.0,    "expected_tami": 0.75},
        {"t": 0.5,  "expected_ammi": 1.0,    "expected_tami": 0.5},
        {"t": 0.75, "expected_ammi": 0.6667, "expected_tami": 0.5},
        {"t": 0.9,  "expected_ammi": 0.5556, "expected_tami": 0.5},
        {"t": 0.6,  "expected_ammi": 0.8333, "expected_tami": 0.5},
        {"t": 0.33, "expected_ammi": 1.0,    "expected_tami": 0.67},
        {"t": 0.1,  "expected_ammi": 1.0,    "expected_tami": 0.9}
    ]

    for i, test in enumerate(tests):
        t = test["t"]
        result = compute_optimal_allocation(t)
        ammi = round(result['ammi_value'], 4)
        tami = round(result['tami_value'], 4)
        status = result['status']

        expected_ammi = round(test["expected_ammi"], 4)
        expected_tami = round(test["expected_tami"], 4)

        # בדיקת קנאה: תמי מקנאת אם הערך שהיא מייחסת למה שעמי קיבל גדול ממה שהיא קיבלה
        tx = t * ammi
        envy = tami < tx

        print(f"\n🧪 Test {i + 1} | t = {t}")
        print(f"   Ammi: expected {expected_ammi}, got {ammi}")
        print(f"   Tami: expected {expected_tami}, got {tami}")
        print(f"   Status: {status}")
        print(f"   Does Tami envy Ammi? {'😡 Yes' if envy else '😊 No'}")

        if math.isclose(ammi, expected_ammi, abs_tol=1e-3) and math.isclose(tami, expected_tami, abs_tol=1e-3) and status == 'optimal':
            print("✅ Test passed!")
        else:
            print("❌ Test FAILED.")


if __name__ == "__main__":
    run_manual_tests()
