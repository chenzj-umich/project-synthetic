# from ulab import numpy as np
import numpy as np

class Mat:
  def add(A, B):
      return np.add(A, B)

  def subtract(A, B):
      return np.subtract(A, B)

  def multiply(A, B):
      return np.dot(A, B)

  def inv(A):
      if np.linalg.det(A) == 0:
          raise ValueError("Matrix is singular and cannot be inverted.")
      return np.linalg.inv(A)

  def det(A):
      return np.linalg.det(A)

# def rotation
# axis: r(x), p(y), y(z)
def rotation_matrix(axis, angle_radians):
    cos_theta, sin_theta = np.cos(angle_radians), np.sin(angle_radians)
    if axis == 'x':
        return np.array([
            [1, 0, 0],
            [0, cos_theta[0], -sin_theta[0]],
            [0, sin_theta[0], cos_theta[0]]
        ])
    elif axis == 'y':
        return np.array([
            [cos_theta[1], 0, sin_theta[1]],
            [0, 1, 0],
            [-sin_theta[1], 0, cos_theta[1]]
        ])
    elif axis == 'z' :
        return np.array([
            [cos_theta[2], -sin_theta[2], 0],
            [sin_theta[2], cos_theta[2], 0],
            [0, 0, 1]
        ])
    elif axis == 'world': # world-fixed frame, roll-pitch-yaw angles
        # TODO:
        Rx = rotation_matrix('x', angle_radians)
        Ry = rotation_matrix('y', angle_radians)
        Rz = rotation_matrix('z', angle_radians)
        return np.dot(Rz, np.dot(Ry, Rx))
    elif axis == 'body': # body-fixed frame, Euler angles
        # TODO:
        Rx = rotation_matrix('x', angle_radians)
        Ry = rotation_matrix('y', angle_radians)
        Rz = rotation_matrix('z', angle_radians)
        return np.dot(Rx, np.dot(Ry, Rz))
    else:
        raise ValueError("Axis must be 'x', 'y', 'z', 'space', or 'body")

# def overriding operator for list
def list_div(self, divisor):
    divided_numbers = [x / divisor for x in self]
    return divided_numbers

def list_add(self, other):
    if len(self) != len(other):
        raise ValueError("Both lists must have the same length for element-wise addition.")
    return [a + b for a, b in zip(self, other)]

def list_sub(self, other):
    if len(self) != len(other):
        raise ValueError("Both lists must have the same length for element-wise addition.")
    return [a - b for a, b in zip(self, other)]
