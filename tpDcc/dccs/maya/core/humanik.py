#!#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains functions and classes to work with HumanIK
"""

from __future__ import print_function, division, absolute_import

import os

import tpDcc as tp
import tpDcc.dccs.maya as maya


class HIKBoneNames(object):
    Hips = 'Hips'
    Head = 'Head'
    LeftArm = 'LeftArm'
    LeftArmRoll = 'LeftArmRoll'
    LeftFoot = 'LeftFoot'
    LeftForeArm = 'LeftForeArm'
    LeftForeArmRoll = 'LeftForeArmRoll'
    LeftHand = 'LeftHand'
    LeftHandIndex1 = 'LeftHandIndex1'
    LeftHandIndex2 = 'LeftHandIndex2'
    LeftHandIndex3 = 'LeftHandIndex3'
    LeftHandMiddle1 = 'LeftHandMiddle1'
    LeftHandMiddle2 = 'LeftHandMiddle2'
    LeftHandMiddle3 = 'LeftHandMiddle3'
    LeftHandPinky1 = 'LeftHandPinky1'
    LeftHandPinky2 = 'LeftHandPinky2'
    LeftHandPinky3 = 'LeftHandPinky3'
    LeftHandRing1 = 'LeftHandRing1'
    LeftHandRing2 = 'LeftHandRing2'
    LeftHandRing3 = 'LeftHandRing3'
    LeftHandThumb1 = 'LeftHandThumb1'
    LeftHandThumb2 = 'LeftHandThumb2'
    LeftHandThumb3 = 'LeftHandThumb3'
    LeftInHandIndex = 'LeftInHandIndex'
    LeftInHandMiddle = 'LeftInHandMiddle'
    LeftInHandPinky = 'LeftInHandPinky'
    LeftInHandRing = 'LeftInHandRing'
    LeftLeg = 'LeftLeg'
    LeftLegRoll = 'LeftLegRoll'
    LeftShoulder = 'LeftShoulder'
    LeftToeBase = 'LeftToeBase'
    LeftUpLeg = 'LeftUpLeg'
    LeftUpLegRoll = 'LeftUpLegRoll'
    Neck = 'Neck'
    Reference = 'Reference'
    RightArm = 'RightArm'
    RightArmRoll = 'RightArmRoll'
    RightFoot = 'RightFoot'
    RightForeArm = 'RightForeArm'
    RightForeArmRoll = 'RightForeArmRoll'
    RightHand = 'RightHand'
    RightHandIndex1 = 'RightHandIndex1'
    RightHandIndex2 = 'RightHandIndex2'
    RightHandIndex3 = 'RightHandIndex3'
    RightHandMiddle1 = 'RightHandMiddle1'
    RightHandMiddle2 = 'RightHandMiddle2'
    RightHandMiddle3 = 'RightHandMiddle3'
    RightHandPinky1 = 'RightHandPinky1'
    RightHandPinky2 = 'RightHandPinky2'
    RightHandPinky3 = 'RightHandPinky3'
    RightHandRing1 = 'RightHandRing1'
    RightHandRing2 = 'RightHandRing2'
    RightHandRing3 = 'RightHandRing3'
    RightHandThumb1 = 'RightHandThumb1'
    RightHandThumb2 = 'RightHandThumb2'
    RightHandThumb3 = 'RightHandThumb3'
    RightInHandIndex = 'RightInHandIndex'
    RightInHandMiddle = 'RightInHandMiddle'
    RightInHandPinky= 'RightInHandPinky'
    RightInHandRing = 'RightInHandRing'
    RightLeg = 'RightLeg'
    RightLegRoll = 'RightLegRoll'
    RightShoulder = 'RightShoulder'
    RightToeBase = 'RightToeBase'
    RightUpLeg = 'RightUpLeg'
    RightUpLegRoll = 'RightUpLegRoll'
    Spine = 'Spine'
    Spine1 = 'Spine1'
    Spine2 = 'Spine2'


HIK_BONES = {
    HIKBoneNames.Hips: {'index': 1},
    HIKBoneNames.Head: {'index': 15},
    HIKBoneNames.LeftArm: {'index': 9},
    HIKBoneNames.LeftArmRoll: {'index': 45},
    HIKBoneNames.LeftFoot: {'index': 4},
    HIKBoneNames.LeftForeArm: {'index': 10},
    HIKBoneNames.LeftForeArmRoll: {'index': 46},
    HIKBoneNames.LeftHand: {'index': 11},
    HIKBoneNames.LeftHandIndex1: {'index': 54},
    HIKBoneNames.LeftHandIndex2: {'index': 55},
    HIKBoneNames.LeftHandIndex3: {'index': 56},
    HIKBoneNames.LeftHandMiddle1: {'index': 58},
    HIKBoneNames.LeftHandMiddle2: {'index': 59},
    HIKBoneNames.LeftHandMiddle3: {'index': 60},
    HIKBoneNames.LeftHandPinky1: {'index': 66},
    HIKBoneNames.LeftHandPinky2: {'index': 67},
    HIKBoneNames.LeftHandPinky3: {'index': 68},
    HIKBoneNames.LeftHandRing1: {'index': 62},
    HIKBoneNames.LeftHandRing2: {'index': 63},
    HIKBoneNames.LeftHandRing3: {'index': 64},
    HIKBoneNames.LeftHandThumb1: {'index': 50},
    HIKBoneNames.LeftHandThumb2: {'index': 51},
    HIKBoneNames.LeftHandThumb3: {'index': 52},
    HIKBoneNames.LeftInHandIndex: {'index': 147},
    HIKBoneNames.LeftInHandMiddle: {'index': 148},
    HIKBoneNames.LeftInHandRing: {'index': 149},
    HIKBoneNames.LeftInHandPinky: {'index': 150},
    HIKBoneNames.LeftLeg: {'index': 3},
    HIKBoneNames.LeftLegRoll: {'index': 42},
    HIKBoneNames.LeftShoulder: {'index': 18},
    HIKBoneNames.LeftToeBase: {'index': 16},
    HIKBoneNames.LeftUpLeg: {'index': 2},
    HIKBoneNames.LeftUpLegRoll: {'index': 41},
    HIKBoneNames.Neck: {'index': 20},
    HIKBoneNames.Reference: {'index': 0},
    HIKBoneNames.RightArm: {'index': 12},
    HIKBoneNames.RightArmRoll: {'index': 47},
    HIKBoneNames.RightFoot: {'index': 7},
    HIKBoneNames.RightForeArm: {'index': 13},
    HIKBoneNames.RightForeArmRoll: {'index': 48},
    HIKBoneNames.RightHand: {'index': 14},
    HIKBoneNames.RightHandIndex1: {'index': 78},
    HIKBoneNames.RightHandIndex2: {'index': 79},
    HIKBoneNames.RightHandIndex3: {'index': 80},
    HIKBoneNames.RightHandMiddle1: {'index': 82},
    HIKBoneNames.RightHandMiddle2: {'index': 83},
    HIKBoneNames.RightHandMiddle3: {'index': 84},
    HIKBoneNames.RightHandPinky1: {'index': 90},
    HIKBoneNames.RightHandPinky2: {'index': 91},
    HIKBoneNames.RightHandPinky3: {'index': 92},
    HIKBoneNames.RightHandRing1: {'index': 86},
    HIKBoneNames.RightHandRing2: {'index': 87},
    HIKBoneNames.RightHandRing3: {'index': 88},
    HIKBoneNames.RightHandThumb1: {'index': 74},
    HIKBoneNames.RightHandThumb2: {'index': 75},
    HIKBoneNames.RightHandThumb3: {'index': 76},
    HIKBoneNames.RightInHandIndex: {'index': 153},
    HIKBoneNames.RightInHandMiddle: {'index': 154},
    HIKBoneNames.RightInHandRing: {'index': 155},
    HIKBoneNames.RightInHandPinky: {'index': 156},
    HIKBoneNames.RightLeg: {'index': 6},
    HIKBoneNames.RightLegRoll: {'index': 44},
    HIKBoneNames.RightShoulder: {'index': 19},
    HIKBoneNames.RightToeBase: {'index': 17},
    HIKBoneNames.RightUpLeg: {'index': 5},
    HIKBoneNames.RightUpLegRoll: {'index': 43},
    HIKBoneNames.Spine: {'index': 8},
    HIKBoneNames.Spine1: {'index': 23},
    HIKBoneNames.Spine2: {'index': 24}
}


def load_human_ik_plugin():
    """
    Load all required HumanIK commands and plugins
    """

    maya_location = os.getenv('MAYA_LOCATION', None)
    if not maya_location or not os.path.isdir(maya_location):
        maya.logger.warning(
            'Impossible to load HumanIK commands/plugins because Maya location was not found: {}!'.format(
                maya_location))
        return False

    # Source HumanIK files
    maya.eval('source "' + maya_location + '/scripts/others/hikGlobalUtils.mel"')
    maya.eval('source "' + maya_location + '/scripts/others/hikCharacterControlsUI.mel"')
    maya.eval('source "' + maya_location + '/scripts/others/hikDefinitionOperations.mel"')
    maya.eval('source "' + maya_location + '/scripts/others/CharacterPipeline.mel"')
    maya.eval('source "' + maya_location + '/scripts/others/characterSelector.mel"')

    # Load HumanIK plugins
    if not tp.Dcc.is_plugin_loaded('mayaHIK'):
        tp.Dcc.load_plugin('mayaHIK')
    if not tp.Dcc.is_plugin_loaded('mayaCharacterization'):
        tp.Dcc.load_plugin('mayaCharacterization')
    if not tp.Dcc.is_plugin_loaded('retargeterNodes'):
        tp.Dcc.load_plugin('retargeterNodes')

    # HIK Character Controls Tool
    maya.eval('HIKCharacterControlsTool')

    return True


def initialize():
    """
    Makes sure that HumanIK tool is laoded and visible
    """

    if maya.mel.eval('exists hikGetCurrentCharacter'):
        character = get_current_character()
    else:
        character = ''

    maya.mel.eval('HIKCharacterControlsTool();')

    maya.set_current_character(character)


def update_hik_tool():
    """
    Refreshes HumanIK tool UI so that fits the current HumanIK character
    """

    maya.mel.eval("""
    if (hikIsCharacterizationToolUICmdPluginLoaded())
    {
        hikUpdateCharacterList();
        hikUpdateSourceList();
        hikUpdateContextualUI();
    }
    """)


def none_string():
    """
    Returns the string that should be display when no HumanIK character is selected
    :return: str
    """
    try:
        return maya.mel.eval('hikNoneString()') or ''
    except Exception:
        return ''


def create_character(character_name, character_namespace=None, lock=True):
    """
    Creates a HumanIK character and tries to use the given name to name the new character
    :param character_name: str, name of the new HumanIK character
    """

    if character_namespace and not character_namespace.endswith(':'):
        character_namespace = '{}:'.format(character_namespace)
    character_namespace = character_namespace or ''

    character_definition = maya.mel.eval('hikCreateCharacter("{0}")'.format(character_name))
    set_current_character(character_definition)

    try:
        maya.mel.eval('hikUpdateCharacterList()')
        maya.mel.eval('hikSelectDefinitionTab()')
    except Exception:
        pass

    for bone_name, bone_data in HIK_BONES.items():
        bone_full_name = '{}{}'.format(character_namespace, bone_name)
        if not tp.Dcc.object_exists(bone_full_name):
            maya.logger.warning('HIK bone "{}" not found in scene!'.format(bone_name))
            continue
        bone_index = bone_data['index']
        set_character_object(character_definition, bone_full_name, bone_index, 0)

    property_node = get_properties_node(character_definition)

    tp.Dcc.set_attribute_value(property_node, 'ForceActorSpace', 0)
    tp.Dcc.set_attribute_value(property_node, 'ScaleCompensationMode', 1)
    tp.Dcc.set_attribute_value(property_node, 'Mirror', 0)
    tp.Dcc.set_attribute_value(property_node, 'HipsHeightCompensationMode', 1)
    tp.Dcc.set_attribute_value(property_node, 'AnkleProximityCompensationMode', 1)
    tp.Dcc.set_attribute_value(property_node, 'AnkleHeightCompensationMode', 0)
    tp.Dcc.set_attribute_value(property_node, 'MassCenterCompensationMode', 1)

    if lock:
        maya.mel.eval('hikToggleLockDefinition')

    return character_definition


def rename_character(character):
    """
    Opens a dialog that allows the user to rename the given HumanIK character
    """

    maya.mel.eval('hikSetCurrentCharacter("{0}");  hikRenameDefinition();'.format(character))


def get_current_character():
    """
    Returns the name of the current HumanIK character
    :return: str
    """

    return maya.mel.eval('hikGetCurrentCharacter()') or 'None'


def set_current_character(character):
    """
    Sets the given HumanIK character as the global current HumanIK
    """

    maya.mel.eval('hikSetCurrentCharacter("{}");'.format(character))
    maya.mel.eval('hikUpdateCharacterList()')
    maya.mel.eval('hikSetCurrentSourceFromCharacter("{}")'.format(character))
    maya.mel.eval('hikUpdateSourceList()')


def get_character_nodes(node):
    """
    Returns all character nodes in the given HumanIk character definition node
    :param node: str
    :return: list(str
    """

    if not is_character_definition(node):
        raise Exception(
            'Invalid character definition node! Object "{}" does not exists or '
            'is not a valid HIKCharacterNode!'.format(node))

    character_nodes = maya.mel.eval('hikGetSkeletonNodes "{}"'.format(node))

    return character_nodes

def get_scene_characters():
    """
    Returns a list of names for all HumanIK characters in the current scene
    """

    return maya.mel.eval('hikGetSceneCharacters()') or []


def delete_whole_character(character):
    """
    Deletes the given HumanIK character
    It deletes its control rig (if any), its skeleton (if any) and its character definition
    """

    maya.mel.eval("""
    hikSetCurrentCharacter("{0}"); hikDeleteControlRig(); hikDeleteSkeleton_noPrompt();
    """.format(character))


def get_skeleton_generator_node(character):
    """
    Returns the name of the skeleton generator node associated with teh given HumanIK
    character if it exists, or an empty string otherwise
    :param character: str, HumanIK character name
    """

    return maya.mel.eval('hikGetSkeletonGeneratorNode("{0}")'.format(character)) or ''


def is_character_definition(node):
    """
    Returns whether or not given node is an HumanIK character node
    :param node: str
    :return: bool
    """

    if not tp.Dcc.object_exists(node):
        return False

    if tp.Dcc.object_type(node) != 'HIKCharacterNode':
        return False

    return True


def is_character_definition_locked(node):
    """
    Returns whether or not given HumanIK character node is locked
    :param node: str
    :return: bool
    """

    if not is_character_definition(node):
        raise Exception(
            'Invalid character definition node! Object "{}" does not exists or '
            'is not a valid HIKCharacterNode!'.format(node))

    lock = maya.cmds.getAttr('{}.InputCharacterizationLock'.format(node))

    return lock


def set_character_definition_lock_status(node, lock_state=True):
    """
    Sets the lock status of the given HumanIk character definition
    :param node: str
    :param lock_state: bool
    :return: int, lock state
    """

    if not is_character_definition(node):
        raise Exception(
            'Invalid character definition node! Object "{}" does not exists or '
            'is not a valid HIKCharacterNode!'.format(node))

    is_locked = is_character_definition_locked(node)

    if lock_state != is_locked:
        maya.mel.eval('hikToggleLockDefinition')

    return int(lock_state)


def set_character_source(character_node, source):
    """
    Sets current character source
    :param character_node: str
    :param source: str
    """

    # HIK Character Controls Tool
    maya.mel.eval('HIKCharacterControlsTool')

    current_character = get_current_character()
    set_current_character(character_node)

    # set character source
    maya.mel.eval('hikSetCurrentSource("{}")'.format(source))
    maya.mel.eval('hikUpdateSourceList()')
    maya.mel.eval('hikUpdateCurrentSourceFromUI()')
    maya.mel.eval('hikUpdateContextualUI()')
    maya.mel.eval('hikControlRigSelectionChangedCallback')

    # restore current character
    if character_node != current_character:
        set_current_character(current_character)


def set_character_object(character_node, character_bone, bone_id, delete_bone=False):
    """
    Sets a node in the given character definition
    :param character_node: str
    :param character_bone: str
    :param bone_id: str
    :param delete_bone: bool
    :return:
    """

    maya.mel.eval(
        'setCharacterObject("{}", "{}", "{}", "{}")'.format(
            character_bone, character_node, str(bone_id), str(int(delete_bone))))


def get_properties_node(character_node):
    """
    Returns HIKProperty2State node of the given HumanIk Character node
    :param character_node: str
    :return: str
    """

    if not is_character_definition(character_node):
        raise Exception(
            'Invalid character definition node! Object "{}" does not exists or '
            'is not a valid HIKCharacterNode!'.format(character_node))

    try:
        property_node = maya.mel.eval('getProperty2StateFromCharacter("{}")'.format(character_node))
    except Exception:
        connections = maya.cmds.listConnections('{}.propertyState'.format(character_node), s=True, d=False)
        if not connections:
            raise Exception(
                'Unable to determine HIKProperty2State nodef rom character definition node "{}"!'.format(
                    character_node))

        if len(connections) > 1:
            maya.logger.warning(
                'Multiple HIKProperty2State nodes found for character definition "{}"! '
                'Returning first item only ...'.format(character_node))

        property_node = connections[0]

    return property_node


def get_solver_node(character_node):
    """
    Returns HIKSolverNode  node of the given HumanIk Character node
    :param character_node: str
    :return: str
    """

    if not is_character_definition(character_node):
        raise Exception(
            'Invalid character definition node! Object "{}" does not exists or '
            'is not a valid HIKCharacterNode!'.format(character_node))

    connections = maya.cmds.ls(maya.cmds.listConnections(
        '{}.OutputPropertySetState'.format(character_node), d=True, s=False) or list(), type='HIKSolverNode')
    if not connections:
        raise Exception('Unable to determine HIKSolverNode from character definition node "{}"!'.format(character_node))

    if len(connections) > 1:
        maya.logger.warning(
            'Multiple HIKSolverNode nodes found for character definition "{}"! Returning first item only ...'.format(
                character_node))

    return connections[0]


def get_retarget_node(character_node):
    """
    Returns HIKRetargeterNode   node of the given HumanIk Character node
    :param character_node: str
    :return: str
    """

    if not is_character_definition(character_node):
        raise Exception(
            'Invalid character definition node! Object "{}" does not exists or '
            'is not a valid HIKCharacterNode!'.format(character_node))

    connections = maya.cmds.ls(maya.cmds.listConnections(
        '{}.OutputPropertySetState'.format(character_node), d=True, s=False) or list(), type='HIKRetargeterNode')
    if not connections:
        raise Exception('Unable to determine HIKRetargeterNode from character definition node "{}"!'.format(
            character_node))

    if len(connections) > 1:
        maya.logger.warning(
            'Multiple HIKRetargeterNode  nodes found for character definition "{}"! '
            'Returning first item only ...'.format(character_node))

    return connections[0]


def bake_animation(character_node):
    """
    Bakes the animation of the given character node
    :param character_node: str
    :return: list(str), list of bones used for the animation baking process
    """

    bones = get_character_nodes(character_node)

    maya.cmds.bakeResult(
        bones, simulation=True, t=[1, 55], sampleBy=1, disableImplicitControl=True, preserveOutsideKeys=False,
        sparseAnimCurveBake=False, removeBakedAttributeFromLayer=False, bakeOnOverrideLayer=False,
        minimizeRotation=False, at=['tx','ty','tz','rx','ry','rz'])

    return bones