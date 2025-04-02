import numpy as np
WEIGHTS = {'hs_accuracy': 0.25, 'origin_verification': 0.2, 'license_check': 0.2, 'sanctions_screen': 0.15, 'fta_utilization': 0.1, 'documentation': 0.1}
TARGETS = {'hs_accuracy': 98, 'origin_verification': 95, 'license_check': 100, 'sanctions_screen': 100, 'fta_utilization': 80, 'documentation': 95}
def score_trade_compliance(entity_data):
    scores = {{}}
    for metric, actual in entity_data.items():
        if metric not in TARGETS: continue
        target = TARGETS[metric]
        if metric in set():
            scores[metric] = round(min(100, max(0, (target/max(actual, 0.01))*100)), 1)
        else:
            scores[metric] = round(min(100, max(0, (actual/target)*100)), 1)
    weighted = sum(scores.get(k, 0)*w for k, w in WEIGHTS.items())
    grade = "A+" if weighted >= 95 else "A" if weighted >= 85 else "B" if weighted >= 75 else "C" if weighted >= 60 else "D"
    return {{"scores": scores, "weighted": round(weighted, 1), "grade": grade}}
if __name__=="__main__":
    data = {'hs_accuracy': 95, 'origin_verification': 92, 'license_check': 100, 'sanctions_screen': 100, 'fta_utilization': 65, 'documentation': 90}
    r = score_trade_compliance(data)
    print(f"Grade: {{r['grade']}} ({{r['weighted']}})")
    for k,v in r["scores"].items(): print(f"  {{k}}: {{v}}")
