import bpy
import math

scene = bpy.context.scene
fps = scene.render.fps

# Set the timeline
scene.frame_start = 1
scene.frame_end = 1920

# Get metarig object
metarig = bpy.data.objects["metarig"]
camera = bpy.data.objects["Camera"]

# Starting camera position

camera.location = (2, -5.8, 2.8)
camera.keyframe_insert(data_path="location", frame=1)
camera.keyframe_insert(data_path="location", frame=60)

camera.rotation_mode = 'XYZ'
camera.rotation_euler = (math.radians(90), 0, 0)
camera.keyframe_insert(data_path="rotation_euler", frame=1)
#camera.keyframe_insert(data_path="rotation_euler", frame=2500)

camera.location = (0, -16, 3.55)
camera.keyframe_insert(data_path="location", frame=70)
#camera.keyframe_insert(data_path="location", frame=2500)


# Starting metarig position
metarig.location = (2, 0, 3.941)
metarig.keyframe_insert(data_path="location", frame=1)
metarig.keyframe_insert(data_path="location", frame=45)

armature = metarig.pose

spine = armature.bones["spine"]
spine.rotation_mode = 'XYZ'

spine.rotation_euler = (math.radians(111.485), math.radians(249.485),  math.radians(-90))
spine.keyframe_insert(data_path="rotation_euler", frame=1)
spine.keyframe_insert(data_path="rotation_euler", frame=3)

spine.rotation_euler = (math.radians(176), math.radians(176),  math.radians(-182))
spine.keyframe_insert(data_path="rotation_euler", frame=10)
spine.keyframe_insert(data_path="rotation_euler", frame=44)

spine.rotation_euler = (math.radians(176), math.radians(197),  math.radians(-178))
spine.keyframe_insert(data_path="rotation_euler", frame=50)
spine.keyframe_insert(data_path="rotation_euler", frame=52)

spine.rotation_euler = (math.radians(176), math.radians(176),  math.radians(-182))
spine.keyframe_insert(data_path="rotation_euler", frame=56)
#spine.keyframe_insert(data_path="rotation_euler", frame=2500)

# Arms posed in position from part one
armature.bones["upper_arm.L"].rotation_mode = 'XYZ'
armature.bones["upper_arm.R"].rotation_mode = 'XYZ'

armature.bones["upper_arm.L"].rotation_euler = (math.radians(-25), 0, math.radians(1))
armature.bones["upper_arm.R"].rotation_euler = (math.radians(90), math.radians(50), math.radians(21))
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=1)
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=1)
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=52)
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=7)

armature.bones["forearm.L"].rotation_mode = 'XYZ'
armature.bones["forearm.R"].rotation_mode = 'XYZ'

armature.bones["forearm.L"].rotation_euler = (math.radians(-45), math.radians(-15), math.radians(-13))
armature.bones["forearm.R"].rotation_euler = (math.radians(55), math.radians(15), math.radians(13))
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=1)
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=1)
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=52)
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=7)

# Spine for head in position from part one
armature.bones["spine.005"].rotation_mode = 'XYZ'
armature.bones["spine.006"].rotation_mode = 'XYZ'

#armature.bones["spine.005"].rotation_euler = (math.radians(-5.00787), math.radians(-48.778), math.radians(14.6334))
#armature.bones["spine.005"].keyframe_insert(data_path="rotation_euler", frame=1)
#armature.bones["spine.005"].keyframe_insert(data_path="rotation_euler", frame=3)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=1)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=10)

# Turn to the camera actions
armature.bones["spine.005"].rotation_euler = (math.radians(-22), math.radians(-10), math.radians(7))
armature.bones["spine.005"].keyframe_insert(data_path="rotation_euler", frame=1)
armature.bones["spine.005"].keyframe_insert(data_path="rotation_euler", frame=3)

armature.bones["spine.005"].rotation_euler = (math.radians(2), math.radians(0), math.radians(0))
armature.bones["spine.005"].keyframe_insert(data_path="rotation_euler", frame=6)
armature.bones["spine.005"].keyframe_insert(data_path="rotation_euler", frame=236)

armature.bones["forearm.R"].rotation_euler = (math.radians(12), math.radians(15), math.radians(13))
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=10)
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=52)

armature.bones["upper_arm.R"].rotation_euler = (math.radians(90), math.radians(24), math.radians(21))
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=10)
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=52)

# Move to sit down
metarig.location = (0, -0.85, 4.35)
metarig.keyframe_insert(data_path="location", frame=60)
#metarig.keyframe_insert(data_path="location", frame=2500)


armature.bones["thigh.L"].rotation_mode = 'XYZ' # thighs rotation on x = -15
armature.bones["thigh.R"].rotation_mode = 'XYZ'

armature.bones["thigh.L"].rotation_euler = (0, 0, 0)
armature.bones["thigh.R"].rotation_euler = (0, 0, 0)
armature.bones["thigh.L"].keyframe_insert(data_path="rotation_euler", frame=1)
armature.bones["thigh.R"].keyframe_insert(data_path="rotation_euler", frame=1)
armature.bones["thigh.L"].keyframe_insert(data_path="rotation_euler", frame=60)
armature.bones["thigh.R"].keyframe_insert(data_path="rotation_euler", frame=60)

armature.bones["thigh.L"].rotation_euler = (math.radians(-15), 0, 0)
armature.bones["thigh.R"].rotation_euler = (math.radians(-15), 0, 0)
armature.bones["thigh.L"].keyframe_insert(data_path="rotation_euler", frame=61)
armature.bones["thigh.R"].keyframe_insert(data_path="rotation_euler", frame=61)



armature.bones["upper_arm.L"].rotation_euler = (math.radians(50), math.radians(4), math.radians(15))
armature.bones["upper_arm.R"].rotation_euler = (math.radians(50), math.radians(-4), math.radians(-15))
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=61)
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=61)
#armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=55)
#armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=55)

armature.bones["forearm.L"].rotation_euler = (math.radians(40), math.radians(-37), math.radians(-43))
armature.bones["forearm.R"].rotation_euler = (math.radians(40), math.radians(37), math.radians(43))
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=63)
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=63)
#armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=55)
#armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=55)


armature.bones["upper_arm.L"].rotation_euler = (math.radians(45), math.radians(-45), math.radians(30))
armature.bones["upper_arm.R"].rotation_euler = (math.radians(45), math.radians(45), math.radians(-30))
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=65)
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=65)
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=69)
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=69)

armature.bones["forearm.L"].rotation_euler = (math.radians(45), math.radians(-66), math.radians(-13))
armature.bones["forearm.R"].rotation_euler = (math.radians(45), math.radians(66), math.radians(13))
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=65)
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=65)
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=69)
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=69)


armature.bones["upper_arm.L"].rotation_euler = (math.radians(45), math.radians(-32), math.radians(32))
armature.bones["upper_arm.R"].rotation_euler = (math.radians(38), math.radians(32), math.radians(-32))
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=75)
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=75)

armature.bones["forearm.L"].rotation_euler = (math.radians(10), math.radians(-32), math.radians(-20))
armature.bones["forearm.R"].rotation_euler = (math.radians(10), math.radians(32), math.radians(20))
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=75)
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=75)


armature.bones["upper_arm.L"].rotation_euler = (math.radians(60), 0, math.radians(26))
armature.bones["upper_arm.R"].rotation_euler = (math.radians(60), 0, math.radians(-26))
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=80)
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=80)
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=86)
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=86)

armature.bones["forearm.L"].rotation_euler = (math.radians(10), math.radians(-32), math.radians(-5))
armature.bones["forearm.R"].rotation_euler = (math.radians(10), math.radians(32), math.radians(5))
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=80)
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=80)
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=160)
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=262)


# After frame 86, we try to get the Lizard Spy to lean downwards

armature.bones["upper_arm.L"].rotation_euler = (math.radians(42), math.radians(31), math.radians(16))
armature.bones["upper_arm.R"].rotation_euler = (math.radians(42), math.radians(-31), math.radians(-16))
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=90)
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=90)
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=160)
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=262)


# Then after frame 160, Lizard proudly beats on chest

armature.bones["upper_arm.L"].rotation_euler = (math.radians(58), math.radians(6), math.radians(20))
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=165)

armature.bones["forearm.L"].rotation_euler = (math.radians(55), math.radians(-3), math.radians(-44))
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=165)

armature.bones["upper_arm.L"].rotation_euler = (math.radians(67), math.radians(11), math.radians(18))
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=170)

armature.bones["forearm.L"].rotation_euler = (math.radians(76), math.radians(31), math.radians(-57))
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=170)


armature.bones["upper_arm.L"].rotation_euler = (math.radians(57), math.radians(5), math.radians(19))
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=173)

armature.bones["forearm.L"].rotation_euler = (math.radians(65), math.radians(12), math.radians(-50))
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=173)

armature.bones["upper_arm.L"].rotation_euler = (math.radians(67), math.radians(11), math.radians(18))
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=176)

armature.bones["forearm.L"].rotation_euler = (math.radians(76), math.radians(31), math.radians(-57))
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=176)

armature.bones["upper_arm.L"].rotation_euler = (math.radians(57), math.radians(5), math.radians(19))
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=179)

armature.bones["forearm.L"].rotation_euler = (math.radians(65), math.radians(12), math.radians(-50))
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=179)

armature.bones["upper_arm.L"].rotation_euler = (math.radians(67), math.radians(11), math.radians(18))
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=182)
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=236)

armature.bones["forearm.L"].rotation_euler = (math.radians(76), math.radians(31), math.radians(-57))
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=236)


# Frame 230 retract back and hand goes back

armature.bones["spine.002"].rotation_mode = 'XYZ'
armature.bones["spine.003"].rotation_mode = 'XYZ'
armature.bones["spine.004"].rotation_mode = 'XYZ'

armature.bones["spine.002"].rotation_euler = (0, 0, 0)
armature.bones["spine.003"].rotation_euler = (0, 0, 0)
armature.bones["spine.004"].rotation_euler = (0, 0, 0)
armature.bones["spine.002"].keyframe_insert(data_path="rotation_euler", frame=1)
armature.bones["spine.003"].keyframe_insert(data_path="rotation_euler", frame=1)
armature.bones["spine.004"].keyframe_insert(data_path="rotation_euler", frame=1)
armature.bones["spine.002"].keyframe_insert(data_path="rotation_euler", frame=236)
armature.bones["spine.003"].keyframe_insert(data_path="rotation_euler", frame=236)
armature.bones["spine.004"].keyframe_insert(data_path="rotation_euler", frame=236)

armature.bones["spine.002"].rotation_euler = (math.radians(-5), 0, 0)
armature.bones["spine.003"].rotation_euler = (math.radians(-5), 0, 0)
armature.bones["spine.004"].rotation_euler = (math.radians(-5), 0, 0)
armature.bones["spine.005"].rotation_euler = (math.radians(-5), 0, 0)
armature.bones["spine.002"].keyframe_insert(data_path="rotation_euler", frame=240)
armature.bones["spine.003"].keyframe_insert(data_path="rotation_euler", frame=240)
armature.bones["spine.004"].keyframe_insert(data_path="rotation_euler", frame=240)
armature.bones["spine.005"].keyframe_insert(data_path="rotation_euler", frame=240)
armature.bones["spine.002"].keyframe_insert(data_path="rotation_euler", frame=262)
armature.bones["spine.003"].keyframe_insert(data_path="rotation_euler", frame=262)
armature.bones["spine.004"].keyframe_insert(data_path="rotation_euler", frame=262)
armature.bones["spine.005"].keyframe_insert(data_path="rotation_euler", frame=262)

# Return spines 2-4 back in place right after
armature.bones["spine.002"].rotation_euler = (0, 0, 0)
armature.bones["spine.003"].rotation_euler = (0, 0, 0)
armature.bones["spine.004"].rotation_euler = (0, 0, 0)
armature.bones["spine.002"].keyframe_insert(data_path="rotation_euler", frame=270)
armature.bones["spine.003"].keyframe_insert(data_path="rotation_euler", frame=270)
armature.bones["spine.004"].keyframe_insert(data_path="rotation_euler", frame=270)

armature.bones["upper_arm.L"].rotation_euler = (math.radians(42), math.radians(31), math.radians(16))
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=240)
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=262)

armature.bones["forearm.L"].rotation_euler = (math.radians(10), math.radians(-32), math.radians(-5))
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=240)
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=262)


# Following frame 270, Lizard tilts his head confused

armature.bones["spine.006"].rotation_euler = (math.radians(5), math.radians(1), math.radians(20))
armature.bones["spine.005"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=270)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=424)
armature.bones["spine.005"].keyframe_insert(data_path="rotation_euler", frame=270)
armature.bones["spine.005"].keyframe_insert(data_path="rotation_euler", frame=340)

armature.bones["upper_arm.L"].rotation_euler = (math.radians(76), math.radians(-12), math.radians(-33))
armature.bones["upper_arm.R"].rotation_euler = (math.radians(68), math.radians(-28), math.radians(-24))
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=270)
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=270)
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=340)
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=461)

armature.bones["forearm.L"].rotation_euler = (math.radians(63), math.radians(-15), math.radians(-54))
armature.bones["forearm.R"].rotation_euler = (math.radians(82), math.radians(-3), math.radians(38))
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=270)
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=270)
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=340)
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=461)


# From frame 340, have them look down and tap their face
armature.bones["spine.005"].rotation_euler = (math.radians(26), math.radians(-30), math.radians(-2))
armature.bones["spine.005"].keyframe_insert(data_path="rotation_euler", frame=345)
armature.bones["spine.005"].keyframe_insert(data_path="rotation_euler", frame=426)

armature.bones["upper_arm.L"].rotation_euler = (math.radians(78), math.radians(-8), math.radians(-12))
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=345)
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=457)

armature.bones["forearm.L"].rotation_euler = (math.radians(80), math.radians(-1), math.radians(-52))
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=345)
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=425)

# Moving Hands during this part
armature.bones["hand.L"].rotation_mode = 'XYZ'

armature.bones["hand.L"].rotation_euler = (0, 0, 0)
armature.bones["hand.L"].keyframe_insert(data_path="rotation_euler", frame=1)
armature.bones["hand.L"].keyframe_insert(data_path="rotation_euler", frame=344)

start_frame_for_hands = 345
end_frame_for_hands = 420                # End this when Lizard dismisses confusion
cycle_length_for_hands = 4               # frames per hand sway
sway_angle_for_hands = math.radians(10)

hand_frame = start_frame_for_hands
direction_for_hands = -1

for frame in range(start_frame_for_hands, end_frame_for_hands + 1, cycle_length_for_hands):
    armature.bones["hand.L"].rotation_euler = (direction_for_hands * sway_angle_for_hands, 0, 0)
    armature.bones["hand.L"].keyframe_insert(data_path="rotation_euler", frame=frame)
    direction_for_hands *= -1  # flip between +10 and -10

armature.bones["hand.L"].rotation_euler = (0, 0, 0)
armature.bones["hand.L"].keyframe_insert(data_path="rotation_euler", frame=421)


# Frame 424 should be return to neutral pose and dismissive waving

armature.bones["spine.006"].rotation_euler = (math.radians(-4), math.radians(-22), math.radians(16))
armature.bones["spine.005"].rotation_euler = (math.radians(1), math.radians(-28), math.radians(-18))
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=430)
armature.bones["spine.005"].keyframe_insert(data_path="rotation_euler", frame=430)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=457)
armature.bones["spine.005"].keyframe_insert(data_path="rotation_euler", frame=457)

armature.bones["forearm.L"].rotation_euler = (math.radians(42), math.radians(-31), math.radians(-16))
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=426)
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=457)

start_frame_for_hands_2 = 426
end_frame_for_hands_2 = 456                # End this when Lizard dismisses confusion
cycle_length_for_hands_2 = 4               # frames per hand sway
sway_angle_for_hands_2 = math.radians(10)

hand_frame_2 = start_frame_for_hands
direction_for_hands_2 = -1

for frame in range(start_frame_for_hands_2, end_frame_for_hands_2 + 1, cycle_length_for_hands_2):
    armature.bones["hand.L"].rotation_euler = (0, direction_for_hands_2 * sway_angle_for_hands, 0)
    armature.bones["hand.L"].keyframe_insert(data_path="rotation_euler", frame=frame)
    direction_for_hands_2 *= -1  # flip between +10 and -10

armature.bones["hand.L"].rotation_euler = (0, 0, 0)
armature.bones["hand.L"].keyframe_insert(data_path="rotation_euler", frame=457)

# Let's finally return to normal... Frames 461-466

armature.bones["upper_arm.R"].rotation_euler = (math.radians(42), math.radians(-31), math.radians(-16))
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=466)
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=682)
armature.bones["forearm.R"].rotation_euler = (math.radians(10), math.radians(32), math.radians(5))
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=466)
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=682)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.005"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=465)
armature.bones["spine.005"].keyframe_insert(data_path="rotation_euler", frame=465)

armature.bones["upper_arm.L"].rotation_euler = (math.radians(56), math.radians(-34), math.radians(-2))
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=466)
armature.bones["upper_arm.L"].rotation_euler = (math.radians(80), math.radians(8), math.radians(-20))
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=508)
armature.bones["forearm.L"].rotation_euler = (math.radians(10), math.radians(16), math.radians(8))
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=466)
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=508)

armature.bones["upper_arm.L"].rotation_euler = (math.radians(42), math.radians(31), math.radians(16))
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=514)
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=682)
armature.bones["forearm.L"].rotation_euler = (math.radians(10), math.radians(-32), math.radians(-5))
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=514)
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=682)


# Explaining Da Rules Motions of raising arms

armature.bones["upper_arm.R"].rotation_euler = (math.radians(22), math.radians(37), math.radians(-5))
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=692)
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=774)
armature.bones["forearm.R"].rotation_euler = (math.radians(87), math.radians(38), math.radians(28))
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=692)
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=774)

armature.bones["upper_arm.L"].rotation_euler = (math.radians(22), math.radians(-37), math.radians(5))
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=692)
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=774)
armature.bones["forearm.L"].rotation_euler = (math.radians(87), math.radians(-38), math.radians(-28))
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=692)
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=774)

armature.bones["upper_arm.R"].rotation_euler = (math.radians(-52), math.radians(-14), math.radians(-10))
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=784)
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=1263)
armature.bones["forearm.R"].rotation_euler = (math.radians(76), math.radians(-34), math.radians(24))
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=784)
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=1263)

armature.bones["upper_arm.L"].rotation_euler = (math.radians(-52), math.radians(14), math.radians(10))
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=784)
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=950)
armature.bones["forearm.L"].rotation_euler = (math.radians(76), math.radians(34), math.radians(-24))
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=784)
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=950)

# Phone Time!

phone = bpy.data.objects["Phone"]

start_frame_for_phone = 930
end_frame_for_phone = 1005
total_frames_for_phone = end_frame_for_phone - start_frame_for_phone
start_z = 11
end_z = 3  # adjust this to match your character’s hand height
spiral_radius = 0.2  # adjust for tighter/wider spiral

# Insert initial position keyframe
phone.location = (0, 0, start_z)
phone.keyframe_insert(data_path="location", frame=start_frame_for_phone)

for frame in range(start_frame_for_phone, end_frame_for_phone + 1):
    progress_for_phone = (frame - start_frame_for_phone) / total_frames_for_phone
    z = start_z - (start_z - end_z) * progress_for_phone
    
    # Spiral movement
    angle_for_phone = progress_for_phone * 8 * math.pi  # 4 rotations
    x = math.cos(angle_for_phone) * spiral_radius + 1
    y = math.sin(angle_for_phone) * spiral_radius

    phone.location = (x, y, z)
    phone.keyframe_insert(data_path="location", frame=frame)


armature.bones["spine.005"].rotation_euler = (0, 0, 0)
armature.bones["spine.004"].rotation_euler = (0, 0, 0)
armature.bones["spine.003"].rotation_euler = (0, 0, 0)
armature.bones["spine.002"].rotation_euler = (0, 0, 0)
armature.bones["spine.005"].keyframe_insert(data_path="rotation_euler", frame=950)
armature.bones["spine.004"].keyframe_insert(data_path="rotation_euler", frame=950)
armature.bones["spine.003"].keyframe_insert(data_path="rotation_euler", frame=950)
armature.bones["spine.002"].keyframe_insert(data_path="rotation_euler", frame=950)

armature.bones["spine.005"].rotation_euler = (math.radians(-6), math.radians(1), math.radians(1))
armature.bones["spine.004"].rotation_euler = (math.radians(-16), math.radians(2), math.radians(1))
armature.bones["spine.003"].rotation_euler = (math.radians(-2), math.radians(1), math.radians(2))
armature.bones["spine.002"].rotation_euler = (math.radians(-5), math.radians(1), math.radians(10))
armature.bones["spine.005"].keyframe_insert(data_path="rotation_euler", frame=965)
armature.bones["spine.004"].keyframe_insert(data_path="rotation_euler", frame=965)
armature.bones["spine.003"].keyframe_insert(data_path="rotation_euler", frame=965)
armature.bones["spine.002"].keyframe_insert(data_path="rotation_euler", frame=965)
armature.bones["spine.005"].keyframe_insert(data_path="rotation_euler", frame=1014)
armature.bones["spine.004"].keyframe_insert(data_path="rotation_euler", frame=1014)
armature.bones["spine.003"].keyframe_insert(data_path="rotation_euler", frame=1014)
armature.bones["spine.002"].keyframe_insert(data_path="rotation_euler", frame=1014)


armature.bones["upper_arm.L"].rotation_euler = (math.radians(-18), math.radians(10), math.radians(8))
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=955)
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=957)
armature.bones["forearm.L"].rotation_euler = (math.radians(20), math.radians(20), math.radians(-12))
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=955)
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=957)

armature.bones["upper_arm.L"].rotation_euler = (math.radians(-29), math.radians(22), math.radians(12))
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=1000)
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=1255)
armature.bones["forearm.L"].rotation_euler = (math.radians(-6), 0, math.radians(71))
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=1000)
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=1255)

armature.bones["spine.005"].rotation_euler = (0, 0, 0)
armature.bones["spine.004"].rotation_euler = (0, 0, 0)
armature.bones["spine.003"].rotation_euler = (0, 0, 0)
armature.bones["spine.002"].rotation_euler = (0, 0, 0)
armature.bones["spine.005"].keyframe_insert(data_path="rotation_euler", frame=1020)
armature.bones["spine.004"].keyframe_insert(data_path="rotation_euler", frame=1020)
armature.bones["spine.003"].keyframe_insert(data_path="rotation_euler", frame=1020)
armature.bones["spine.002"].keyframe_insert(data_path="rotation_euler", frame=1020)

phone.location = (1.2, -0.3, 3)
phone.keyframe_insert(data_path="location", frame=1006)
phone.keyframe_insert(data_path="location", frame=1014)
phone.location = (1.2, -0.6, 3)
phone.keyframe_insert(data_path="location", frame=1019)
phone.keyframe_insert(data_path="location", frame=1255)


# Falling Phone Method

start_frame_falling = 1255
end_frame_falling = 1270
total_frames_falling = end_frame_falling - start_frame_falling

start_loc = (1.2, -0.6, 3)
end_loc = (1.44, 3.8641, 0.0829)
start_rot = (0, 0, 0)
end_rot = (math.radians(-270), 0, 0)

# Calculate apex height (we'll add ~2 units upward to make it arch)
apex_z = max(start_loc[2], end_loc[2]) + 2

for i, frame in enumerate(range(start_frame_falling, end_frame_falling + 1)):
    t = (i) / total_frames_falling  # progress from 0 to 1

    # Smoothstep for natural easing
    smooth_t = t * t * (3 - 2 * t)

    # Interpolate X and Y linearly
    x = start_loc[0] + (end_loc[0] - start_loc[0]) * smooth_t
    y = start_loc[1] + (end_loc[1] - start_loc[1]) * smooth_t

    # Interpolate Z with parabola (up to apex, then down)
    if smooth_t < 0.5:
        z = start_loc[2] + (apex_z - start_loc[2]) * (smooth_t * 2)
    else:
        z = apex_z + (end_loc[2] - apex_z) * ((smooth_t - 0.5) * 2)

    # Interpolate rotation
    rot_x = start_rot[0] + (end_rot[0] - start_rot[0]) * smooth_t
    rot_y = start_rot[1]
    rot_z = start_rot[2]

    phone.location = (x, y, z)
    phone.rotation_euler = (rot_x, rot_y, rot_z)

    phone.keyframe_insert(data_path="location", frame=frame)
    phone.keyframe_insert(data_path="rotation_euler", frame=frame)


armature.bones["upper_arm.L"].rotation_euler = (math.radians(-25), math.radians(23), math.radians(28))
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=1257)
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=1258)

armature.bones["upper_arm.L"].rotation_euler = (math.radians(-23), math.radians(31), math.radians(64))
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=1260)
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=1263)
armature.bones["forearm.L"].rotation_euler = (math.radians(5), 0, math.radians(37))
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=1260)
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=1263)

# Final Part of animation

armature.bones["upper_arm.L"].rotation_euler = (math.radians(42), math.radians(31), math.radians(16))
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=1268)
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=1700)

armature.bones["forearm.L"].rotation_euler = (math.radians(10), math.radians(-32), math.radians(-5))
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=1268)
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=1700)


armature.bones["upper_arm.R"].rotation_euler = (math.radians(42), math.radians(-31), math.radians(-16))
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=1268)
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=1505)
armature.bones["forearm.R"].rotation_euler = (math.radians(10), math.radians(32), math.radians(5))
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=1268)
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=1505)


armature.bones["upper_arm.R"].rotation_euler = (math.radians(72), math.radians(24), math.radians(-26))
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=1510)
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=1700)
armature.bones["forearm.R"].rotation_euler = (math.radians(22), math.radians(42), math.radians(-16))
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=1510)
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=1700)


armature.bones["upper_arm.L"].rotation_euler = (math.radians(50), math.radians(-44), math.radians(10))
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=1706)
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=1805)
armature.bones["forearm.L"].rotation_euler = (math.radians(35), math.radians(-38), math.radians(40))
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=1706)
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=1805)

armature.bones["upper_arm.R"].rotation_euler = (math.radians(50), math.radians(44), math.radians(-10))
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=1706)
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=1805)
armature.bones["forearm.R"].rotation_euler = (math.radians(35), math.radians(38), math.radians(-40))
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=1706)
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=1805)


armature.bones["upper_arm.L"].rotation_euler = (math.radians(44), math.radians(-38), math.radians(8))
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=1810)
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=1890)
armature.bones["forearm.L"].rotation_euler = (math.radians(74), math.radians(30), math.radians(-42))
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=1810)
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=1890)

armature.bones["upper_arm.R"].rotation_euler = (math.radians(44), math.radians(32), math.radians(6))
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=1810)
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=1890)
armature.bones["forearm.R"].rotation_euler = (math.radians(52), math.radians(-40), math.radians(32))
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=1810)
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=1890)


# Clapping animation

armature.bones["upper_arm.L"].rotation_euler = (math.radians(52), math.radians(-16), math.radians(3))
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=1905)
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=1908)
armature.bones["forearm.L"].rotation_euler = (math.radians(74), math.radians(30), math.radians(-42))
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=1905)
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=1908)

armature.bones["upper_arm.R"].rotation_euler = (math.radians(58), math.radians(8), math.radians(17))
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=1905)
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=1908)
armature.bones["forearm.R"].rotation_euler = (math.radians(52), math.radians(-40), math.radians(32))
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=1905)
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=1908)



armature.bones["upper_arm.L"].rotation_euler = (math.radians(52), math.radians(-16), math.radians(3))
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=1911)
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=1914)
armature.bones["forearm.L"].rotation_euler = (math.radians(93.762), math.radians(6.2681), math.radians(6.7454))
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=1911)
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=1914)

armature.bones["upper_arm.R"].rotation_euler = (math.radians(58), math.radians(8), math.radians(17))
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=1911)
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=1914)
armature.bones["forearm.R"].rotation_euler = (math.radians(45.022), math.radians(-33.548), math.radians(20.885))
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=1911)
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=1914)


armature.bones["upper_arm.L"].rotation_euler = (math.radians(52), math.radians(-16), math.radians(3))
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=1917)
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=1920)
armature.bones["forearm.L"].rotation_euler = (math.radians(74), math.radians(30), math.radians(-42))
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=1917)
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=1920)

armature.bones["upper_arm.R"].rotation_euler = (math.radians(58), math.radians(8), math.radians(17))
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=1917)
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=1920)
armature.bones["forearm.R"].rotation_euler = (math.radians(52), math.radians(-40), math.radians(32))
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=1917)
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=1920)


# Leg sway animation during the scene

armature.bones["shin.L"].rotation_mode = 'XYZ'
armature.bones["shin.R"].rotation_mode = 'XYZ'

armature.bones["shin.L"].rotation_euler = (0, 0, 0)
armature.bones["shin.R"].rotation_euler = (0, 0, 0)
armature.bones["shin.L"].keyframe_insert(data_path="rotation_euler", frame=1)
armature.bones["shin.R"].keyframe_insert(data_path="rotation_euler", frame=1)
armature.bones["shin.L"].keyframe_insert(data_path="rotation_euler", frame=60)
armature.bones["shin.R"].keyframe_insert(data_path="rotation_euler", frame=60)

start_frame = 61
end_frame = 1780 # End this and return to a neutral stance when we say "Does this make sense"?
cycle_length = 70  # frames per full sway (down → up → down)
sway_angle = -20    # degrees

frame = start_frame
direction = -1  # start swinging down

while frame <= end_frame:
    angle_rad = math.radians(direction * sway_angle)
    if frame < 1750:
        armature.bones["shin.L"].rotation_euler = (angle_rad, 0, 0)
        armature.bones["shin.L"].keyframe_insert(data_path="rotation_euler", frame=frame)
        
        armature.bones["shin.R"].rotation_euler = (-angle_rad, 0, 0)
        armature.bones["shin.R"].keyframe_insert(data_path="rotation_euler", frame=frame)
    
    # Flip direction and move to next keyframe
        direction *= -1
        frame += cycle_length // 2  # switch every half cycle
    else:
        armature.bones["shin.L"].rotation_euler = (0, 0, 0)
        armature.bones["shin.L"].keyframe_insert(data_path="rotation_euler", frame=frame)
        
        armature.bones["shin.R"].rotation_euler = (0, 0, 0)
        armature.bones["shin.R"].keyframe_insert(data_path="rotation_euler", frame=frame)

        armature.bones["shin.L"].rotation_euler = (angle_rad/4, 0, 0)
        armature.bones["shin.L"].keyframe_insert(data_path="rotation_euler", frame=frame+40)
        
        armature.bones["shin.R"].rotation_euler = (-angle_rad/4, 0, 0)
        armature.bones["shin.R"].keyframe_insert(data_path="rotation_euler", frame=frame+40)

        armature.bones["shin.L"].rotation_euler = (-angle_rad/2, 0, 0)
        armature.bones["shin.L"].keyframe_insert(data_path="rotation_euler", frame=frame+80)
        
        armature.bones["shin.R"].rotation_euler = (angle_rad/2, 0, 0)
        armature.bones["shin.R"].keyframe_insert(data_path="rotation_euler", frame=frame+80)

        armature.bones["shin.L"].rotation_euler = (0, 0, 0)
        armature.bones["shin.L"].keyframe_insert(data_path="rotation_euler", frame=frame+120)
        
        armature.bones["shin.R"].rotation_euler = (0, 0, 0)
        armature.bones["shin.R"].keyframe_insert(data_path="rotation_euler", frame=frame+120)
    
        frame += 1000 # We just want to get out of the while loop


# Tail swaying throughout the duration
tail_bones = [f"spine.{i:03}" for i in range(10, 16)]  # Focus on back of tail
for i, bone_name in enumerate(tail_bones):
    bone = armature.bones[bone_name]
    bone.rotation_mode = 'XYZ'
    bone.location.z -= 0.1  # lift tail bones upward for camera

    for f in range(1, 2500, 10):  # sway every 10 frames
        angle = math.radians(25 * math.sin(f / 15 + i))  # wider radius
        bone.rotation_euler.y = angle
        bone.keyframe_insert(data_path="rotation_euler", frame=f)