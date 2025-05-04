import bpy
import math

scene = bpy.context.scene
fps = scene.render.fps

# Set the timeline
scene.frame_start = 1
scene.frame_end = 2500

# Get metarig object
metarig = bpy.data.objects["metarig"]
camera = bpy.data.objects["Camera"]

# Starting camera position

camera.location = (0, -16, 3.55)
camera.keyframe_insert(data_path="location", frame=1)
camera.keyframe_insert(data_path="location", frame=86)

camera.rotation_mode = 'XYZ'
camera.rotation_euler = (math.radians(66), 0, 0)
camera.keyframe_insert(data_path="rotation_euler", frame=1)
camera.keyframe_insert(data_path="rotation_euler", frame=15)

# All camera movement

camera.rotation_euler = (math.radians(90), 0, 0)
camera.keyframe_insert(data_path="rotation_euler", frame=40)

camera.rotation_euler = (math.radians(85), 0, math.radians(5))
camera.keyframe_insert(data_path="rotation_euler", frame=49)

camera.rotation_euler = (math.radians(90), 0, math.radians(10))
camera.keyframe_insert(data_path="rotation_euler", frame=58)
camera.keyframe_insert(data_path="rotation_euler", frame=69)

camera.rotation_euler = (math.radians(96), 0, math.radians(10))
camera.keyframe_insert(data_path="rotation_euler", frame=76)
camera.keyframe_insert(data_path="rotation_euler", frame=86)

camera.rotation_euler = (math.radians(90), 0, math.radians(-12))
camera.keyframe_insert(data_path="rotation_euler", frame=96)
camera.keyframe_insert(data_path="rotation_euler", frame=250)

camera.location = (5.8, -9.6, 2.3)
camera.keyframe_insert(data_path="location", frame=96)
camera.keyframe_insert(data_path="location", frame=130)

camera.location = (0, -9.6, 2.3)
camera.keyframe_insert(data_path="location", frame=230)
camera.keyframe_insert(data_path="location", frame=250)

camera.location = (2, -5.8, 2.8)
camera.keyframe_insert(data_path="location", frame=280)

camera.rotation_euler = (math.radians(90), 0, 0)
camera.keyframe_insert(data_path="rotation_euler", frame=275)

# Starting metarig position
metarig.location = (12, 0, 3.941)
metarig.keyframe_insert(data_path="location", frame=1)
metarig.keyframe_insert(data_path="location", frame=60)

armature = metarig.pose
armature.bones["spine"].rotation_mode = 'XYZ'
armature.bones["spine"].rotation_euler = (math.radians(111.485), math.radians(249.485), math.radians(-90))
armature.bones["spine"].keyframe_insert(data_path="rotation_euler", frame=1)
armature.bones["spine"].keyframe_insert(data_path="rotation_euler", frame=302)

# Arms posed behind back
armature.bones["upper_arm.L"].rotation_mode = 'XYZ'
armature.bones["upper_arm.R"].rotation_mode = 'XYZ'

armature.bones["upper_arm.L"].rotation_euler = (math.radians(-25), 0, math.radians(-10))
armature.bones["upper_arm.R"].rotation_euler = (math.radians(-25), 0, math.radians(10))
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=1)
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=1)
armature.bones["upper_arm.L"].keyframe_insert(data_path="rotation_euler", frame=121)
armature.bones["upper_arm.R"].keyframe_insert(data_path="rotation_euler", frame=121)

armature.bones["forearm.L"].rotation_mode = 'XYZ'
armature.bones["forearm.R"].rotation_mode = 'XYZ'

armature.bones["forearm.L"].rotation_euler = (math.radians(-45), math.radians(-15), math.radians(-13))
armature.bones["forearm.R"].rotation_euler = (math.radians(-45), math.radians(15), math.radians(13))
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=1)
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=1)
armature.bones["forearm.L"].keyframe_insert(data_path="rotation_euler", frame=121)
armature.bones["forearm.R"].keyframe_insert(data_path="rotation_euler", frame=121)

# Walk cycle to the chair
leg_bones = ["thigh.L", "thigh.R", "shin.L", "shin.R", "foot.L", "foot.R"]
for bone_name in leg_bones:
    bone = armature.bones[bone_name]
    bone.rotation_mode = 'XYZ'

walk_start = 69
walk_end = 260
steps = 9  # number of walk cycles
step_frames = (walk_end - walk_start) // steps

for i in range(steps + 1):
    f = walk_start + i * step_frames
    angle = math.radians(30 if i % 2 == 0 else -30)
    armature.bones["thigh.L"].rotation_euler.x = angle
    armature.bones["thigh.R"].rotation_euler.x = -angle
    armature.bones["thigh.L"].keyframe_insert(data_path="rotation_euler", frame=f)
    armature.bones["thigh.R"].keyframe_insert(data_path="rotation_euler", frame=f)

# Metarig arrives at chair
metarig.location = (2, 0, 3.941)
metarig.keyframe_insert(data_path="location", frame=260)

# Turn around
#armature.bones["spine"].rotation_euler = (0, 0, 0)  # Face camera
#armature.bones["spine"].keyframe_insert(data_path="rotation_euler", frame=366)

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

# Head movement
armature.bones["spine.005"].rotation_mode = 'XYZ'
armature.bones["spine.005"].rotation_euler = (0, math.radians(46), 0)
armature.bones["spine.005"].keyframe_insert(data_path="rotation_euler", frame=1)
armature.bones["spine.005"].keyframe_insert(data_path="rotation_euler", frame=129)

armature.bones["spine.006"].rotation_mode = 'XYZ'
armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=1)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=89)

# "You are all finally awake."
armature.bones["spine.006"].rotation_euler = (math.radians(-15), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=91)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=92)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=94)

armature.bones["spine.006"].rotation_euler = (math.radians(-15), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=96)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=97)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=99)

armature.bones["spine.006"].rotation_euler = (math.radians(-15), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=101)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=102)

armature.bones["spine.006"].rotation_euler = (math.radians(-15), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=104)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=105)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=107)

armature.bones["spine.006"].rotation_euler = (math.radians(-15), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=108)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=110)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=112)

armature.bones["spine.006"].rotation_euler = (math.radians(-15), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=114)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=116)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=119)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=130)

#
# Rotate the Left upper_arm by x = -15, then by y = 50
# Then do the same with the forearm with x = -15, then by y = 50
# 
# Then both upper_arm and forearm again after that by another y = 60
#
# Flip it for the Right Arm, Make the negatives for the x positive, same y
#

# Bones to modify
left_upper = armature.bones["upper_arm.L"]
right_upper = armature.bones["upper_arm.R"]
left_forearm = armature.bones["forearm.L"]
right_forearm = armature.bones["forearm.R"]

# Set rotation mode to XYZ Euler to avoid quaternion confusion
for bone in [left_upper, right_upper, left_forearm, right_forearm]:
    bone.rotation_mode = 'XYZ'

# Add x and y rotation on top of current pose (frame 124 → 126)

# Left side: y -= 15, x += 50
left_upper.rotation_euler.x += math.radians(50)
left_upper.rotation_euler.y += math.radians(-15)
left_upper.keyframe_insert(data_path="rotation_euler", frame=129)
left_upper.keyframe_insert(data_path="rotation_euler", frame=129)

left_forearm.rotation_euler.x += math.radians(50)
left_forearm.rotation_euler.y += math.radians(-15)
left_forearm.keyframe_insert(data_path="rotation_euler", frame=129)
left_forearm.keyframe_insert(data_path="rotation_euler", frame=129)

# Right side: y += 15, x += 50
right_upper.rotation_euler.x += math.radians(50)
right_upper.rotation_euler.y += math.radians(15)
right_upper.keyframe_insert(data_path="rotation_euler", frame=129)
right_upper.keyframe_insert(data_path="rotation_euler", frame=129)

right_forearm.rotation_euler.x += math.radians(50)
right_forearm.rotation_euler.y += math.radians(15)
right_forearm.keyframe_insert(data_path="rotation_euler", frame=129)
right_forearm.keyframe_insert(data_path="rotation_euler", frame=129)

# Add extra x rotation (frame 127 → 131)

# Left side: x += 60
left_upper.rotation_euler.x += math.radians(60)
left_upper.keyframe_insert(data_path="rotation_euler", frame=138)
left_upper.keyframe_insert(data_path="rotation_euler", frame=140)

left_forearm.rotation_euler.x += math.radians(60)
left_forearm.keyframe_insert(data_path="rotation_euler", frame=138)
left_forearm.keyframe_insert(data_path="rotation_euler", frame=140)

# Right side: x += 60
right_upper.rotation_euler.x += math.radians(60)
right_upper.keyframe_insert(data_path="rotation_euler", frame=138)
right_upper.keyframe_insert(data_path="rotation_euler", frame=140)

right_forearm.rotation_euler.x += math.radians(60)
right_forearm.keyframe_insert(data_path="rotation_euler", frame=138)
right_forearm.keyframe_insert(data_path="rotation_euler", frame=140)

# Move arms across the z
left_upper.rotation_euler.z += math.radians(1)
left_upper.keyframe_insert(data_path="rotation_euler", frame=139)
left_upper.rotation_euler.z += math.radians(20)
left_upper.keyframe_insert(data_path="rotation_euler", frame=168)
left_upper.keyframe_insert(data_path="rotation_euler", frame=170)

right_upper.rotation_euler.z += math.radians(1)
right_upper.keyframe_insert(data_path="rotation_euler", frame=139)
right_upper.rotation_euler.z += math.radians(20)
right_upper.keyframe_insert(data_path="rotation_euler", frame=168)
right_upper.keyframe_insert(data_path="rotation_euler", frame=170)


# "Welcome to our headquarters!"
armature.bones["spine.005"].rotation_euler = (0, 0, 0)
armature.bones["spine.005"].keyframe_insert(data_path="rotation_euler", frame=131)
armature.bones["spine.005"].keyframe_insert(data_path="rotation_euler", frame=177)

armature.bones["spine.006"].rotation_euler = (math.radians(-12), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=131)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=132)

armature.bones["spine.006"].rotation_euler = (math.radians(-12), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=133)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=134)

armature.bones["spine.006"].rotation_euler = (math.radians(-12), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=136)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=137)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=138)

armature.bones["spine.006"].rotation_euler = (math.radians(-9), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=144)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=145)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=146)

armature.bones["spine.006"].rotation_euler = (math.radians(-9), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=148)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=149)

armature.bones["spine.006"].rotation_euler = (math.radians(-9), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=150)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=151)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=152)

armature.bones["spine.006"].rotation_euler = (math.radians(-12), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=154)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=156)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=158)

armature.bones["spine.006"].rotation_euler = (math.radians(-12), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=160)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=162)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=164)

armature.bones["spine.006"].rotation_euler = (math.radians(-12), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=166)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=168)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=173)

# Now let's return the arms back to where they were

# Move arms back from where they are the z-axis
left_upper.rotation_euler.z -= math.radians(10)
left_upper.keyframe_insert(data_path="rotation_euler", frame=178)

right_upper.rotation_euler.z -= math.radians(10)
right_upper.keyframe_insert(data_path="rotation_euler", frame=178)


# Go back from the y rotation

# Left side: x += 60
left_upper.rotation_euler.x -= math.radians(60)
left_upper.keyframe_insert(data_path="rotation_euler", frame=172)
left_upper.keyframe_insert(data_path="rotation_euler", frame=175)

left_forearm.rotation_euler.x -= math.radians(60)
left_forearm.keyframe_insert(data_path="rotation_euler", frame=172)
left_forearm.keyframe_insert(data_path="rotation_euler", frame=175)

# Right side: x += 60
right_upper.rotation_euler.x -= math.radians(60)
right_upper.keyframe_insert(data_path="rotation_euler", frame=172)
right_upper.keyframe_insert(data_path="rotation_euler", frame=175)

right_forearm.rotation_euler.x -= math.radians(60)
right_forearm.keyframe_insert(data_path="rotation_euler", frame=172)
right_forearm.keyframe_insert(data_path="rotation_euler", frame=175)

# Go back to the x and y rotation on top of current pose

# Left side: y -= 15, x += 50
left_upper.rotation_euler.x -= math.radians(50)
left_upper.rotation_euler.y -= math.radians(-15)
left_upper.keyframe_insert(data_path="rotation_euler", frame=178)
left_upper.keyframe_insert(data_path="rotation_euler", frame=180)

left_forearm.rotation_euler.x -= math.radians(50)
left_forearm.rotation_euler.y -= math.radians(-15)
left_forearm.keyframe_insert(data_path="rotation_euler", frame=178)
left_forearm.keyframe_insert(data_path="rotation_euler", frame=180)

# Right side: y += 15, x += 50
right_upper.rotation_euler.x -= math.radians(50)
right_upper.rotation_euler.y -= math.radians(15)
right_upper.keyframe_insert(data_path="rotation_euler", frame=178)
right_upper.keyframe_insert(data_path="rotation_euler", frame=180)

right_forearm.rotation_euler.x -= math.radians(50)
right_forearm.rotation_euler.y -= math.radians(15)
right_forearm.keyframe_insert(data_path="rotation_euler", frame=178)
right_forearm.keyframe_insert(data_path="rotation_euler", frame=180)


# "Or at least the part you are in for now."
armature.bones["spine.005"].rotation_euler = (0, math.radians(46), 0)
armature.bones["spine.005"].keyframe_insert(data_path="rotation_euler", frame=180)
armature.bones["spine.005"].keyframe_insert(data_path="rotation_euler", frame=242)

armature.bones["spine.006"].rotation_euler = (math.radians(-9), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=180)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=181)

armature.bones["spine.006"].rotation_euler = (math.radians(-12), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=182)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=183)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=184)

armature.bones["spine.006"].rotation_euler = (math.radians(-12), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=185)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=186)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=188)

armature.bones["spine.006"].rotation_euler = (math.radians(-12), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=190)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=191)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=192)

armature.bones["spine.006"].rotation_euler = (math.radians(-12), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=194)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=195)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=197)

armature.bones["spine.006"].rotation_euler = (math.radians(-9), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=198)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=199)

armature.bones["spine.006"].rotation_euler = (math.radians(-9), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=200)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=201)

armature.bones["spine.006"].rotation_euler = (math.radians(-9), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=203)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=204)

armature.bones["spine.006"].rotation_euler = (math.radians(-9), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=206)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=208)

armature.bones["spine.006"].rotation_euler = (math.radians(-9), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=211)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=212)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=214)

armature.bones["spine.006"].rotation_euler = (math.radians(-9), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=216)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=218)

armature.bones["spine.006"].rotation_euler = (math.radians(-12), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=220)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=222)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=225)

# "My name is... well..."
armature.bones["spine.005"].rotation_euler = (math.radians(-8), 0, 0)
armature.bones["spine.005"].keyframe_insert(data_path="rotation_euler", frame=244)
armature.bones["spine.005"].keyframe_insert(data_path="rotation_euler", frame=277)

armature.bones["spine.006"].rotation_euler = (math.radians(-12), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=245)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=247)

armature.bones["spine.006"].rotation_euler = (math.radians(-12), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=249)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=251)

armature.bones["spine.006"].rotation_euler = (math.radians(-12), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=253)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=255)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=257)

armature.bones["spine.006"].rotation_euler = (math.radians(-12), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=260)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=262)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=265)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=269)

armature.bones["spine.005"].rotation_euler = (math.radians(-7), math.radians(-10), math.radians(3))
armature.bones["spine.005"].keyframe_insert(data_path="rotation_euler", frame=281)

armature.bones["spine.006"].rotation_euler = (math.radians(-14), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=280)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=282)

armature.bones["spine.006"].rotation_euler = (math.radians(-14), 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=284)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=292)

armature.bones["spine.006"].rotation_euler = (0, 0, 0)
armature.bones["spine.006"].keyframe_insert(data_path="rotation_euler", frame=297)

armature.bones["spine.005"].rotation_euler = (math.radians(-5), math.radians(-50), math.radians(15))
armature.bones["spine.005"].keyframe_insert(data_path="rotation_euler", frame=300)

# Final arm movement for this part

right_upper.rotation_euler.x += math.radians(0)
right_upper.rotation_euler.y += math.radians(0)
right_upper.rotation_euler.y += math.radians(0)
right_upper.keyframe_insert(data_path="rotation_euler", frame=238)

right_forearm.rotation_euler.x += math.radians(0)
right_forearm.rotation_euler.y += math.radians(0)
right_forearm.rotation_euler.y += math.radians(0)
right_forearm.keyframe_insert(data_path="rotation_euler", frame=238)

right_upper.rotation_euler.x += math.radians(50)
right_upper.keyframe_insert(data_path="rotation_euler", frame=241)

right_forearm.rotation_euler.x += math.radians(50)
right_forearm.keyframe_insert(data_path="rotation_euler", frame=241)

right_upper.rotation_euler.x += math.radians(50)
right_upper.keyframe_insert(data_path="rotation_euler", frame=244)

right_upper.rotation_euler.x += math.radians(0)
right_upper.rotation_euler.y += math.radians(0)
right_upper.rotation_euler.y += math.radians(0)
right_upper.keyframe_insert(data_path="rotation_euler", frame=280)

right_forearm.rotation_euler.x += math.radians(50)
right_forearm.keyframe_insert(data_path="rotation_euler", frame=244)

right_forearm.rotation_euler.x += math.radians(0)
right_forearm.rotation_euler.y += math.radians(0)
right_forearm.rotation_euler.y += math.radians(0)
right_forearm.keyframe_insert(data_path="rotation_euler", frame=280)

right_upper.rotation_euler.x += math.radians(15)
right_upper.rotation_euler.y += math.radians(50)
right_upper.rotation_euler.y += math.radians(0)
right_upper.keyframe_insert(data_path="rotation_euler", frame=283)

right_forearm.rotation_euler.x += math.radians(0)
right_forearm.rotation_euler.y += math.radians(0)
right_forearm.rotation_euler.y += math.radians(0)
right_forearm.keyframe_insert(data_path="rotation_euler", frame=283)


# 
# Figuring this out is way too hard. In order to solve this issue,
# Pose the final pose here in a DIFFERENT blender file.
#
# Then from there, continue to the from the line of:
#
# "That's Classified to you, pal!"
#