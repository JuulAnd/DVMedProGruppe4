bl_info = {
    "name": "Tree Materials Add-on",
    "author": "Julia Andräß, Elisabeth Küllmer, Daniel Schlegel",
    "location": "View 3D > Tree Materials",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "description": "Easily add Materials to your tree"
    }
    

import bpy
import os

#Main Panel
class TreeShaderPanel (bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Tree Shaders"
    bl_idname = "TREE_SHADER_PT_tree"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tree Shaders"
    

    def draw(self, context):
        layout = self.layout
        
        
        row = layout.row()
        row.label(text= "Select a Shader for the stem.")
        row = layout.row()
        row.operator('shader.diamond_operator')
        row = layout.row()
        row.operator('shader.wood_operator')
        row = layout.row()
        row.operator('shader.linde_operator')
        row = layout.row()
        row.operator('shader.buche_operator')
        row = layout.row()
        row.operator('shader.birke_operator')
        row = layout.row()
        row.operator('shader.eiche_operator')
        row = layout.row()
        row.operator('shader.euk_operator')
        row = layout.row()
        row.operator('shader.fichte_operator')
        row = layout.row()
        row.operator('shader.lerche_operator')
  
  
#Sub Panel Leaves 
class SubPanelLeaves (bpy.types.Panel):
    bl_label = "Leave Shaders"
    bl_idname = "SHADER_PT_LEAVES"
    bl_space_type = 'VIEW_3D' 
    bl_region_type = 'UI'
    bl_category = 'Tree Shaders'
    bl_parent_id = "TREE_SHADER_PT_tree"
    bl_options = {'DEFAULT_CLOSED'}
    
#Leave Shaders  
    def draw(self, context):
        layout = self.layout 
        layout.scale_y = 1.1
            
        row = layout.row()
        row.label(text= "Select a Shader for the leaves.")
        row = layout.row()
        row.operator('shader.colorful_operator')
        row = layout.row()
        row.operator('shader.fall_operator')
        row = layout.row()
        row.operator('shader.spring_operator')       
        

  
  
#Operator Type, DIAMOND Material
class SHADER_OT_DIAMOND(bpy.types.Operator): 
    bl_label = "Add Diamond"
    bl_idname = 'shader.diamond_operator'
    
    
    def execute(self, context):
        
        #Create new Shader "Diamond"
        material_diamond = bpy.data.materials.new(name="Diamond")
        material_diamond.use_nodes = True
        
        material_diamond.node_tree.nodes.remove(material_diamond.node_tree.nodes.get('Principled BSDF'))
        
        material_output = material_diamond.node_tree.nodes.get('Material Output')
        material_output.location = (400, 0)
        
        glass1_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        glass1_node.location = (-600, 0)
        glass1_node.inputs[0].default_value = (1, 1, 1, 1)
        glass1_node.inputs[2].default_value = 1.446
        
        glass2_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        glass2_node.location = (-600, -150)
        glass2_node.inputs[0].default_value = (1, 1, 1, 1)
        glass2_node.inputs[2].default_value = 1.446
        
        glass3_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        glass3_node.location = (-600, -300)
        glass3_node.inputs[0].default_value = (0, 0, 1, 1)
        glass3_node.inputs[2].default_value = 1.446
        
        
        #Add Shader Node
        add1_node = material_diamond.node_tree.nodes.new('ShaderNodeAddShader')
        add1_node.location = (-400, -50)
        add1_node.label = "Add node"
        add1_node.select = False
        
        
        #Add Shader Node 2
        add2_node = material_diamond.node_tree.nodes.new('ShaderNodeAddShader')
        add2_node.location = (-100, 0)
        add2_node.label = "Add node2"
        add2_node.select = False
        
        
        #Add Glass Node 4
        glass4_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        glass4_node.location = (-150, -150)
        glass4_node.inputs[0].default_value = (1, 1, 1, 1)
        glass4_node.inputs[2].default_value = 1.450
        
        
        #Add Mix Shader Node
        mix1_node = material_diamond.node_tree.nodes.new('ShaderNodeMixShader')
        mix1_node.location = (200, 0)
        mix1_node.select = False
        
        
        #Linking the nodes
        material_diamond.node_tree.links.new(glass1_node.outputs[0], add1_node.inputs[0])
        material_diamond.node_tree.links.new(glass2_node.outputs[0], add1_node.inputs[1])
        material_diamond.node_tree.links.new(add1_node.outputs[0], add2_node.inputs[0])
        material_diamond.node_tree.links.new(glass3_node.outputs[0], add2_node.inputs[1])
        material_diamond.node_tree.links.new(add2_node.outputs[0], mix1_node.inputs[1])
        material_diamond.node_tree.links.new(glass4_node.outputs[0], mix1_node.inputs[2])
        material_diamond.node_tree.links.new(mix1_node.outputs[0], material_output.inputs[0])
        
        
        bpy.context.object.active_material = material_diamond
        bpy.context.space_data.shading.type = 'MATERIAL'

        
        return {'FINISHED'}
    
    
    
    
    
#WOOD Material
class SHADER_OT_WOOD1 (bpy.types.Operator): 
    bl_label = "Add Wood"
    bl_idname = 'shader.wood_operator'
    
    
    def execute(self, context):
        
        #Create new Shader "Wood"
        material_wood = bpy.data.materials.new(name="Wood")
        material_wood.use_nodes = True
        
        material_bsdf = material_wood.node_tree.nodes.get('Principled BSDF')
        material_bsdf.location = (200, 0)
        material_bsdf.inputs[0].default_value = (0.103338, 0.0275888, 0.0203049, 1)
        
        material_output = material_wood.node_tree.nodes.get('Material Output')
        material_output.location = (800, 0) 
    
        material_wood.node_tree.links.new(material_bsdf.outputs[0], material_output.inputs[0])
        
        
        bpy.context.object.active_material = material_wood
        bpy.context.space_data.shading.type = 'MATERIAL'

        
        return {'FINISHED'}
    
    
    
 # Material LINDE 
class SHADER_OT_LINDE (bpy.types.Operator): 
    bl_label = "Add LINDE"
    bl_idname = 'shader.linde_operator'
    
    
    def execute(self, context):
        
        #Create new Shader "WoodImg"
        material_linde = bpy.data.materials.new(name="Linde")
        material_linde.use_nodes = True
        
        material_bsdf = material_linde.node_tree.nodes.get('Principled BSDF')
        material_bsdf.location = (200, 0)
        
        material_output = material_linde.node_tree.nodes.get('Material Output')
        material_output.location = (800, 0) 
        
        #Add Image Texture Node
        img1_node = material_linde.node_tree.nodes.new('ShaderNodeTexImage')
        img1_node.location = (-400, -50)
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        IMAGE_PATH = os.path.join(BASE_PATH, 'Images', 'Lindenrinde.jpg')
        img1_node.image = bpy.data.images.load(IMAGE_PATH)
        img1_node.label = "Add Image Node"
        img1_node.select = False
        
        
        
        #Linking the nodes
        material_linde.node_tree.links.new(img1_node.outputs['Color'], material_bsdf.inputs['Base Color'])
        material_linde.node_tree.links.new(material_bsdf.outputs[0], material_output.inputs[0])
   
        
        
        bpy.context.object.active_material = material_linde
        bpy.context.space_data.shading.type = 'MATERIAL'

        
        return {'FINISHED'}
    
    
    
    
class SHADER_OT_BUCHE (bpy.types.Operator): 
    bl_label = "Add Buche"
    bl_idname = 'shader.buche_operator'
    
    
    def execute(self, context):
        
        #Create new Shader "WoodImg"
        material_buche = bpy.data.materials.new(name="Buche")
        material_buche.use_nodes = True
        
        material_bsdf = material_buche.node_tree.nodes.get('Principled BSDF')
        
        material_bsdf.location = (200, 0)
        
        material_output = material_buche.node_tree.nodes.get('Material Output')
        
        material_output.location = (800, 0) #Location of the node
        
        #Add Image Texture Node
        img1_node = material_buche.node_tree.nodes.new('ShaderNodeTexImage')
        img1_node.location = (-400, -50)
        img1_node.image = bpy.data.images.load("C:\\Users\\julia\\Documents\\Medieninformatik WS 20_21\\Datenverarbeitung\\Buchenrinde.jpg")
        img1_node.label = "Add Image Node"
        img1_node.select = False
        
        
        
        #Linking the nodes
        material_buche.node_tree.links.new(img1_node.outputs['Color'], material_bsdf.inputs['Base Color'])
        material_buche.node_tree.links.new(material_bsdf.outputs[0], material_output.inputs[0])
   
        
        
        bpy.context.object.active_material = material_buche
        bpy.context.space_data.shading.type = 'MATERIAL'

        
        return {'FINISHED'}
    
    

class SHADER_OT_BIRKE (bpy.types.Operator): 
    bl_label = "Add Birke"
    bl_idname = 'shader.birke_operator'
    
    
    def execute(self, context):
        
        #Create new Shader "WoodImg"
        material_birke = bpy.data.materials.new(name="Birke")
        material_birke.use_nodes = True
        
        material_bsdf = material_birke.node_tree.nodes.get('Principled BSDF')
        
        material_bsdf.location = (200, 0)
        
        material_output = material_birke.node_tree.nodes.get('Material Output')
        
        material_output.location = (800, 0) #Location of the node
        
        #Add Image Texture Node
        img1_node = material_birke.node_tree.nodes.new('ShaderNodeTexImage')
        img1_node.location = (-400, -50)
        img1_node.image = bpy.data.images.load("C:\\Users\\julia\\Documents\\Medieninformatik WS 20_21\\Datenverarbeitung\\Birkenrinde.jpg")
        img1_node.label = "Add Image Node"
        img1_node.select = False
        
        
        
        #Linking the nodes
        material_birke.node_tree.links.new(img1_node.outputs['Color'], material_bsdf.inputs['Base Color'])
        material_birke.node_tree.links.new(material_bsdf.outputs[0], material_output.inputs[0])
   
        
        
        bpy.context.object.active_material = material_birke
        bpy.context.space_data.shading.type = 'MATERIAL'

        
        return {'FINISHED'}
    
    



class SHADER_OT_EICHE (bpy.types.Operator): 
    bl_label = "Add Eiche"
    bl_idname = 'shader.eiche_operator'
    
    
    def execute(self, context):
        
        #Create new Shader "WoodImg"
        material_eiche = bpy.data.materials.new(name="Eiche")
        material_eiche.use_nodes = True
        
        material_bsdf = material_eiche.node_tree.nodes.get('Principled BSDF')
        
        material_bsdf.location = (200, 0)
        
        material_output = material_eiche.node_tree.nodes.get('Material Output')
        
        material_output.location = (800, 0) #Location of the node
        
        #Add Image Texture Node
        img1_node = material_eiche.node_tree.nodes.new('ShaderNodeTexImage')
        img1_node.location = (-400, -50)
        img1_node.image = bpy.data.images.load("C:\\Users\\julia\\Documents\\Medieninformatik WS 20_21\\Datenverarbeitung\\Eichenrinde.jpg")
        img1_node.label = "Add Image Node"
        img1_node.select = False
        
        
        
        #Linking the nodes
        material_eiche.node_tree.links.new(img1_node.outputs['Color'], material_bsdf.inputs['Base Color'])
        material_eiche.node_tree.links.new(material_bsdf.outputs[0], material_output.inputs[0])
   
        
        
        bpy.context.object.active_material = material_eiche
        bpy.context.space_data.shading.type = 'MATERIAL'

        
        return {'FINISHED'}
    
    


class SHADER_OT_EUK (bpy.types.Operator): 
    bl_label = "Add Eukalyptus"
    bl_idname = 'shader.euk_operator'
    
    
    def execute(self, context):
        
        #Create new Shader "WoodImg"
        material_euk = bpy.data.materials.new(name="Eukalyptus")
        material_euk.use_nodes = True
        
        material_bsdf = material_euk.node_tree.nodes.get('Principled BSDF')
        
        material_bsdf.location = (200, 0)
        
        material_output = material_euk.node_tree.nodes.get('Material Output')
        
        material_output.location = (800, 0) #Location of the node
        
        #Add Image Texture Node
        img1_node = material_euk.node_tree.nodes.new('ShaderNodeTexImage')
        img1_node.location = (-400, -50)
        img1_node.image = bpy.data.images.load("C:\\Users\\julia\\Documents\\Medieninformatik WS 20_21\\Datenverarbeitung\\Eukrinde.jpg")
        img1_node.label = "Add Image Node"
        img1_node.select = False
        
        
        
        #Linking the nodes
        material_euk.node_tree.links.new(img1_node.outputs['Color'], material_bsdf.inputs['Base Color'])
        material_euk.node_tree.links.new(material_bsdf.outputs[0], material_output.inputs[0])
   
        
        
        bpy.context.object.active_material = material_euk
        bpy.context.space_data.shading.type = 'MATERIAL'

        
        return {'FINISHED'}
    

class SHADER_OT_FICHTE (bpy.types.Operator): 
    bl_label = "Add Fichte"
    bl_idname = 'shader.fichte_operator'
    
    
    def execute(self, context):
        
        #Create new Shader "WoodImg"
        material_fichte = bpy.data.materials.new(name="fichte")
        material_fichte.use_nodes = True
        
        material_bsdf = material_fichte.node_tree.nodes.get('Principled BSDF')
        
        material_bsdf.location = (200, 0)
        
        material_output = material_fichte.node_tree.nodes.get('Material Output')
        
        material_output.location = (800, 0) #Location of the node
        
        #Add Image Texture Node
        img1_node = material_fichte.node_tree.nodes.new('ShaderNodeTexImage')
        img1_node.location = (-400, -50)
        img1_node.image = bpy.data.images.load("C:\\Users\\julia\\Documents\\Medieninformatik WS 20_21\\Datenverarbeitung\\Fichtenrinde.jpg")
        img1_node.label = "Add Image Node"
        img1_node.select = False
        
        
        
        #Linking the nodes
        material_fichte.node_tree.links.new(img1_node.outputs['Color'], material_bsdf.inputs['Base Color'])
        material_fichte.node_tree.links.new(material_bsdf.outputs[0], material_output.inputs[0])
   
        
        
        bpy.context.object.active_material = material_fichte
        bpy.context.space_data.shading.type = 'MATERIAL'

        
        return {'FINISHED'}
    
    
    
    
    
class SHADER_OT_LERCHE (bpy.types.Operator): 
    bl_label = "Add Lärche"
    bl_idname = 'shader.lerche_operator'
    
    
    def execute(self, context):
        
        #Create new Shader "WoodImg"
        material_lerche = bpy.data.materials.new(name="Lärche")
        material_lerche.use_nodes = True
        
        material_bsdf = material_lerche.node_tree.nodes.get('Principled BSDF')
        
        material_bsdf.location = (200, 0)
        
        material_output = material_lerche.node_tree.nodes.get('Material Output')
        
        material_output.location = (800, 0) #Location of the node
        
        #Add Image Texture Node
        img1_node = material_lerche.node_tree.nodes.new('ShaderNodeTexImage')
        img1_node.location = (-400, -50)
        img1_node.image = bpy.data.images.load("C:\\Users\\julia\\Documents\\Medieninformatik WS 20_21\\Datenverarbeitung\\Lärchenrinde.jpg")
        img1_node.label = "Add Image Node"
        img1_node.select = False
        
        
        
        #Linking the nodes
        material_lerche.node_tree.links.new(img1_node.outputs['Color'], material_bsdf.inputs['Base Color'])
        material_lerche.node_tree.links.new(material_bsdf.outputs[0], material_output.inputs[0])
   
        
        
        bpy.context.object.active_material = material_lerche
        bpy.context.space_data.shading.type = 'MATERIAL'

        
        return {'FINISHED'}
    
    
    
    
    
#_______________________________________________________________________________
# Shaders for Leaves


class SHADER_OT_COLORFUL (bpy.types.Operator): 
    bl_label = "Add Colorful"
    bl_idname = 'shader.colorful_operator'
    
    
    def execute(self, context):
        
        #Create new Shader "WoodImg"
        material_colorful = bpy.data.materials.new(name="Colorful")
        material_colorful.use_nodes = True
        
        material_bsdf = material_colorful.node_tree.nodes.get('Principled BSDF')
        
        material_bsdf.location = (200, 0)
        
        material_output = material_colorful.node_tree.nodes.get('Material Output')
        
        material_output.location = (800, 0) #Location of the node
        
        #Add Image Texture Node
        img1_node = material_colorful.node_tree.nodes.new('ShaderNodeTexMagic')
        img1_node.location = (-400, -50)
        img1_node.turbulence_depth = 0
        img1_node.label = "Add Image Node"
        img1_node.select = False
        
        
        
        #Linking the nodes
        material_colorful.node_tree.links.new(img1_node.outputs['Color'], material_bsdf.inputs['Base Color'])
        material_colorful.node_tree.links.new(material_bsdf.outputs[0], material_output.inputs[0])
   
        
        
        bpy.context.object.active_material = material_colorful
        bpy.context.space_data.shading.type = 'MATERIAL'

        
        return {'FINISHED'}





class SHADER_OT_FALL (bpy.types.Operator): 
    bl_label = "Add fall"
    bl_idname = 'shader.fall_operator'
    
    
    def execute(self, context):
        
        #Create new Shader "WoodImg"
        material_fall = bpy.data.materials.new(name="Fall")
        material_fall.use_nodes = True
        
        material_bsdf = material_fall.node_tree.nodes.get('Principled BSDF')
        
        material_bsdf.location = (200, 0)
        material_bsdf.inputs[4].default_value = 0.5
        
        material_output = material_fall.node_tree.nodes.get('Material Output')
        
        material_output.location = (800, 0) #Location of the node
        
        #Add Image Texture Node
        tex1_node = material_fall.node_tree.nodes.new('ShaderNodeTexChecker')
        tex1_node.location = (-400, -50)
        tex1_node.inputs[1].default_value = (0.233016, 0.164378, 0.000186463, 1)
        tex1_node.inputs[2].default_value = (0.199998, 0.0320527, 0.00249657, 1)
        tex1_node.inputs[3].default_value = 10.1
        tex1_node.label = "Add Tex Node"
        tex1_node.select = False
        
        
        
        #Linking the nodes
        material_fall.node_tree.links.new(tex1_node.outputs['Color'], material_bsdf.inputs['Base Color'])
        material_fall.node_tree.links.new(material_bsdf.outputs[0], material_output.inputs[0])
   
        
        
        bpy.context.object.active_material = material_fall
        bpy.context.space_data.shading.type = 'MATERIAL'

        
        return {'FINISHED'}
    


class SHADER_OT_FALL (bpy.types.Operator): 
    bl_label = "Add fall"
    bl_idname = 'shader.fall_operator'
    
    
    def execute(self, context):
        
        #Create new Shader "WoodImg"
        material_fall = bpy.data.materials.new(name="Fall")
        material_fall.use_nodes = True
        
        material_bsdf = material_fall.node_tree.nodes.get('Principled BSDF')
        
        material_bsdf.location = (200, 0)
        material_bsdf.inputs[4].default_value = 0.5
        
        material_output = material_fall.node_tree.nodes.get('Material Output')
        
        material_output.location = (800, 0) #Location of the node
        
        #Add Image Texture Node
        tex1_node = material_fall.node_tree.nodes.new('ShaderNodeTexChecker')
        tex1_node.location = (-400, -50)
        tex1_node.inputs[1].default_value = (0.233016, 0.164378, 0.000186463, 1)
        tex1_node.inputs[2].default_value = (0.199998, 0.0320527, 0.00249657, 1)
        tex1_node.inputs[3].default_value = 10.1
        tex1_node.label = "Add Tex Node"
        tex1_node.select = False
        
        
        
        #Linking the nodes
        material_fall.node_tree.links.new(tex1_node.outputs['Color'], material_bsdf.inputs['Base Color'])
        material_fall.node_tree.links.new(material_bsdf.outputs[0], material_output.inputs[0])
   
        
        
        bpy.context.object.active_material = material_fall
        bpy.context.space_data.shading.type = 'MATERIAL'

        
        return {'FINISHED'}


class SHADER_OT_SPRING (bpy.types.Operator): 
    bl_label = "Add spring"
    bl_idname = 'shader.spring_operator'
    
    
    def execute(self, context):
        
        #Create new Shader "WoodImg"
        material_spring = bpy.data.materials.new(name="Spring")
        material_spring.use_nodes = True
        
        material_bsdf = material_spring.node_tree.nodes.get('Principled BSDF')
        
        material_bsdf.location = (200, 0)
        material_bsdf.inputs[4].default_value = 0.5
        
        material_output = material_spring.node_tree.nodes.get('Material Output')
        material_output.location = (800, 0) 
        
        #Add Brick Texture Node
        brick1_node = material_spring.node_tree.nodes.new('ShaderNodeTexBrick')
        brick1_node.location = (-400, -50)
        brick1_node.inputs[1].default_value = (0.0192992, 0.214036, 0.0147974, 1)
        brick1_node.inputs[2].default_value = (0.00309665, 0.0765796, 0.00543079, 1)
        brick1_node.inputs[3].default_value = (0.0105446)
        
        brick1_node.label = "Add Brick Node"
        brick1_node.select = False
        
        
        
        #Linking the nodes
        material_spring.node_tree.links.new(brick1_node.outputs['Color'], material_bsdf.inputs['Base Color'])
        material_spring.node_tree.links.new(material_bsdf.outputs[0], material_output.inputs[0])
   
        
        
        bpy.context.object.active_material = material_spring
        bpy.context.space_data.shading.type = 'MATERIAL'

        
        return {'FINISHED'}
    
    
def register():
    bpy.utils.register_class(TreeShaderPanel)
    bpy.utils.register_class(SubPanelLeaves)
    bpy.utils.register_class(SHADER_OT_DIAMOND)
    bpy.utils.register_class(SHADER_OT_WOOD1)
    bpy.utils.register_class(SHADER_OT_LINDE)
    bpy.utils.register_class(SHADER_OT_BUCHE)
    bpy.utils.register_class(SHADER_OT_BIRKE)
    bpy.utils.register_class(SHADER_OT_EICHE)
    bpy.utils.register_class(SHADER_OT_FICHTE)
    bpy.utils.register_class(SHADER_OT_EUK)
    bpy.utils.register_class(SHADER_OT_LERCHE)
    
    bpy.utils.register_class(SHADER_OT_COLORFUL)
    bpy.utils.register_class(SHADER_OT_FALL)
    bpy.utils.register_class(SHADER_OT_SPRING)


def unregister():
    bpy.utils.unregister_class(TreeShaderPanel)
    bpy.utils.unregister_class(SubPanelLeaves)
    bpy.utils.unregister_class(SHADER_OT_DIAMOND)
    bpy.utils.unregister_class(SHADER_OT_WOOD1)
    bpy.utils.unregister_class(SHADER_OT_LINDE)
    bpy.utils.unregister_class(SHADER_OT_BUCHE)
    bpy.utils.unregister_class(SHADER_OT_BIRKE)
    bpy.utils.unregister_class(SHADER_OT_EICHE)
    bpy.utils.unregister_class(SHADER_OT_FICHTE)
    bpy.utils.unregister_class(SHADER_OT_EUK)
    bpy.utils.unregister_class(SHADER_OT_LERCHE)
    
    bpy.utils.unregister_class(SHADER_OT_COLORFUL)
    bpy.utils.unregister_class(SHADER_OT_FALL)
    bpy.utils.unregister_class(SHADER_OT_SPRING)




if __name__ == "__main__":
    register()
