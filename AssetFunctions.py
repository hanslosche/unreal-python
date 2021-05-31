import unreal

from importlib import *

texture_tga = '/Users/hlos/testing_unit/unreal-python/Assets/texture.TGA'
sound_wav = '/Users/hlos/testing_unit/unreal-python/Assets/sound.WAV'

def importMyAssets():
    texture_task = buildImportTask(texture_tga, '/Game/Textures')
    sound_task = buildImportTask(sound_wav, '/Game/Sounds')
    executeImportTasks([texture_task, sound_task])

def buildImportTask(filename, destination_path):
    task = unreal.AssetImportTask()
    task.set_editor_property('automated', True)
    task.set_editor_property('destination_name', '')
    task.set_editor_property('destination_path', destination_path)
    task.set_editor_property('filename', filename)
    task.set_editor_property('replace_existing', True)
    task.set_editor_property('save', True)

    return task

def executeImportTasks(tasks):
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)

        
