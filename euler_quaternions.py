# Conversion from euler angles to quaternions

import math

def eulerToQuaternions(euler_angles):
	quaternions = []

	for i in range(0,len(euler_angles)):
		c = [math.cos(euler_angles[i][1] / 2), math.cos(euler_angles[i][2] / 2), math.cos(euler_angles[i][0] / 2)]
		s = [math.sin(euler_angles[i][1] / 2), math.sin(euler_angles[i][2] / 2), math.sin(euler_angles[i][0] / 2)]
		quaternions.append([(c[0]*c[1]*c[2] - s[0]*s[1]*s[2]),
								(s[0]*s[1]*c[2] + c[0]*c[1]*s[2]),
								(s[0]*c[1]*c[2] + c[0]*s[1]*s[2]),
								(c[0]*s[1]*c[2] - s[0]*c[1]*s[2])])
	return quaternion
ss

if __name__ == "__main__":
	orientations = [[3*math.pi/180,2*math.pi/180,math.pi/180], [0,math.pi/180,0]]
	quaternions = eulerToQuaternions(orientations);

	print('Orientations : ', orientations)
	print('\nQuaternions : ', quaternions)