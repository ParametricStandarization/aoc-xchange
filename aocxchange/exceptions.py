#!/usr/bin/python
# coding: utf-8

r"""Exceptions for Aoc Data Exchange"""


class AocXChangeException(Exception):
    r"""Generic Aoc Data Exchange Exception

    Inherit this exception to define more specific exceptions

    """
    pass


class BRepBuildingException(AocXChangeException):
    r"""Something went wrong while building a BRep"""
    pass


# IO Specific / All file types generic


class FileNotFoundException(AocXChangeException):
    r"""The file could not be found"""
    pass


class DirectoryNotFoundException(AocXChangeException):
    r"""The directory could not be found"""
    pass


class IncompatibleFileFormatException(AocXChangeException):
    r"""The file format is not what is expected"""
    pass


class FileReadException(AocXChangeException):
    r"""Something went wrong while reading a file"""
    pass


# IGES Specific


class IgesFileReadException(FileReadException):
    r"""Something wrent wrong while reading an IGES file"""
    pass


class IgesUnknownFormatException(AocXChangeException):
    r"""The IGES format s not 5.1 or 5.3"""
    pass


# STEP Specific


class StepFileReadException(FileReadException):
    r"""Something wrent wrong while reading a STEP file"""
    pass
