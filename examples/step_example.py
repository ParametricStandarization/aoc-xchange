#!/usr/bin/python
# coding: utf-8

r"""STEP.py use example"""

import OCC.BRepPrimAPI

import aocxchange.step


def import_step():
    """
    Imports a STEP file.
    """
    my_importer = aocxchange.step.StepImporter("./models_input/box_203.stp")
    my_importer.read_file()
    print(my_importer.shapes)


def export_step():
    """
    Exports a TopoDS_Shape to a STEP file.
    """
    test_shape = OCC.BRepPrimAPI.BRepPrimAPI_MakeBox(100., 100., 100.).Shape()
    # export to AP203 schema
    ap203_exporter = aocxchange.step.StepExporter('./models_output/box_203.stp', schema='AP203')
    ap203_exporter.add_shape(test_shape)
    ap203_exporter.write_file()
    # export AP214 schema
    ap214cd_exporter = aocxchange.step.StepExporter('./models_output/box_214CD.stp', schema='AP214CD')
    ap214cd_exporter.add_shape(test_shape)
    ap214cd_exporter.write_file()

if __name__ == '__main__':
    export_step()
    import_step()
