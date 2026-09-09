import math

class VirtualStructureFormation:
    """Rigid Virtual Structure Formation Controller."""
    def __init__(self, offsets):
        self.offsets = offsets

    def compute_robot_targets(self, center_pos, heading_angle_rad):
        cx, cy = center_pos
        targets = {}
        cos_theta = math.cos(heading_angle_rad)
        sin_theta = math.sin(heading_angle_rad)

        for rid, (dx, dy) in self.offsets.items():
            rx = dx * cos_theta - dy * sin_theta
            ry = dx * sin_theta + dy * cos_theta
            targets[rid] = [round(cx + rx, 2), round(cy + ry, 2)]
        return targets
