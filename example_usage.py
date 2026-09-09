from client import VirtualStructureFormation

def main():
    print("=== Testing Virtual Structure Formation ===")
    formation = VirtualStructureFormation({
        "lead": [0.0, 0.0],
        "escort_left": [-5.0, -5.0],
        "escort_right": [5.0, -5.0]
    })

    targets = formation.compute_robot_targets([100.0, 200.0], heading_angle_rad=0.0)
    print("Calculated Waypoints:", targets)
    assert targets['lead'] == [100.0, 200.0]
    assert targets['escort_left'] == [95.0, 195.0]
    assert targets['escort_right'] == [105.0, 195.0]

    print("Virtual Structure Formation verified successfully!")

if __name__ == '__main__':
    main()
