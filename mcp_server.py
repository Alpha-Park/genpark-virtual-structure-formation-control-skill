import sys
import json
from client import VirtualStructureFormation

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "get_targets":
        vs = VirtualStructureFormation(params.get("offsets", {}))
        return {"targets": vs.compute_robot_targets(params.get("center", [0, 0]), params.get("heading", 0.0))}
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == '__main__':
    main()
