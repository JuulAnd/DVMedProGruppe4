bl_info = {
    "name":"L-System-Tree",
    "blender":(2,80,0),
    "category":"Object"
}

import bpy

class LSystemTree(bpy.types.Operator):
    bl_idname = "mesh.tree"
    bl_label = "Create Tree with L-Systems"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        #X -> Startpunkt erzeugen
        bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        zylinderhöhe = bpy.context.active_object.dimensions.z      
        
        rulesX = "F+[[X]-X]-F[-FX]+X"
        rulesF = "FF"
        buildingPlan = "X"
        angle = 0
        position = (0,0,0)
        currentAngle = 0
        currentPosition = (0,0,0)
        z = 2
        rounds = 3
               
        while rounds > 0:  

            #in buildingplan entsprechend die Wert ersetzen indem Fall X -> F+[[X]-X]-F[-FX]+X
            buildingPlanArray = buildingPlan.split('#')
            a = 0
            while a < len(buildingPlan):
                if buildingPlanArray [a] == 'X':
                    buildingPlanArray[a] = 'F#+#[#[#X#]#-#X#]#-#F#[#-#F#X#]#+#X'
                    a +=1
                elif buildingPlanArray[a] == 'F':
                    buildingPlanArray[a] = 'F#F'
                    a +=1
                elif a == len(buildingPlanArray):
                    break
            
           #buildingPlan = ''.join(buildingPlanArray)
            index = 0
            buildingPlan = ''
            while index < len(buildingPlanArray):
                buildingPlan += str(buildingPlanArray[index])
                index += 1
                
            buildingPlanArray = buildingPlan.split("#")
            #String nach und nach durchgehen und für
            #F "nach vorne" gehen
            # - currentAngle -25 (25 Grad nach rechts drehen)
            # + currentAngle +25 (25 Grad nach links drehen)
            # alle anderen Zeichen überspringen 
            a = 0
            print(buildingPlan)
            print(buildingPlanArray)
            while a < len(buildingPlanArray):
                if buildingPlanArray[a] == 'F':
                    print('F')
                    bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, enter_editmode=False, align='WORLD', location =  position, scale=(1, 1, 1))
                    bpy.context.active_object.rotation_euler[angle] 
                    a +=1
                elif buildingPlanArray[a] == '-':
                    print('-')
                    angle - 25
                    a +=1
                elif buildingPlanArray[a] == '+':
                    print('+')
                    angle + 25
                    a +=1
               elif buildingPlanArray[a] == '[':
                    print('[')
                    currentAngle = angle
                    currentPosition = position
                    a +=1
                elif buildingPlanArray[a] == ']':
                    print(']')
                    angle = currentAngle
                    position = currentPosition
                    a +=1
                elif a == len(buildingPlanArray):
                    print('a zu groß')
                    break
                else:
                    print('else')
                    a += 1
            
            rounds -=1
            z += zylinderhöhe
        return {'FINISHED'}
                

def register():
    bpy.utils.register_class(LSystemTree)
def unregister():
    bpy.utils.unregister_class(LSystemTree)
    

if __name__ == "__main__":
    register()
    
