
import numpy as np


def deflector(r, phi, z, n_arc):
    '''Wire model geometry of deflector

    Parameters
    ----------
    r : float
        Radius of deflector geometry
    phi : float
        Angular width of deflector mode
    z : float
        Z position of deflector geometry
    n_arc : int
        Number of arcs to use to make up the model

    Returns
    -------
    points_arc_1 : ndarray
        Points of a circle to represent the lens geometry
    points_arc_2 : ndarray
        Points of a circle to represent the lens geometry
    '''

    THETA = np.linspace(-phi, phi, n_arc, endpoint=True)
    R = r*np.ones(np.size(THETA))
    Z = z*np.ones(np.size(THETA))

    points_arc_1 = np.array([R*np.cos(THETA), R*np.sin(THETA), Z])
    points_arc_2 = np.array([-R*np.cos(THETA), -R*np.sin(-THETA), Z])

    return points_arc_1, points_arc_2


def lens(r, z, n_arc):
    '''Wire model geometry of lens

    Parameters
    ----------
    r : float
        Radius of lens geometry
    z : float
        Z position of lens geometry
    n_arc : int
        Number of arcs to use to make up the model

    Returns
    -------
    points_circle : ndarray
        Points of a circle to represent the lens geometry
    '''
    THETA = np.linspace(0, 2*np.pi, n_arc, endpoint=True)
    R = r*np.ones(np.size(THETA))
    Z = z*np.ones(np.size(THETA))

    points_circle = np.array([R*np.cos(THETA), R*np.sin(THETA), Z])

    return points_circle


def biprism(r, z, theta):
    '''Wire model geometry for biprism

    Parameters
    ----------
    r : float
        Radius of wire
    z : float
        Z position of wire
    theta : float
        Angle of wire - Two options, 0 or np.pi/2

    Returns
    -------
    points : ndarray
        Points array of wire geometry
    '''
    THETA = np.array([theta, theta+np.pi])
    R = r*np.ones(np.size(THETA))
    Z = z*np.ones(np.size(THETA))

    points = np.array([R*np.cos(THETA), R*np.sin(THETA), Z])

    return points


def quadrupole(r, phi, z, n_arc):
    '''Wire model geometry of deflector

    Parameters
    ----------
    r : float
        Radius of quadrupole geometry
    phi : float
        Angular width of quadrupole mode
    z : float
        Z position of quadrupole geometry
    n_arc : int
        Number of arcs to use to make up the model

    Returns
    -------
    points_arc_1 : ndarray
        Points of first semi circle that represent the quadrupole geometry
    points_arc_2 : ndarray
        Points of second semi circle that represent the quadrupole geometry
    points_arc_3 : ndarray
        Points of third semi circle that represent the quadrupole geometry
    points_arc_4 : ndarray
        Points of fourth semi circle that represent the quadrupole geometry
    '''

    THETA = np.linspace(-phi, phi, n_arc, endpoint=True)
    R = r*np.ones(np.size(THETA))
    Z = z*np.ones(np.size(THETA))

    points_arc_1 = np.array([R*np.cos(THETA), R*np.sin(THETA), Z])
    points_arc_2 = np.array([-R*np.cos(THETA), -R*np.sin(-THETA), Z])
    points_arc_3 = np.array([R*np.cos(THETA+np.pi/2), R*np.sin(THETA+np.pi/2), Z])
    points_arc_4 = np.array([-R*np.cos(THETA+np.pi/2), -R*np.sin(-THETA+np.pi/2), Z])

    return points_arc_1, points_arc_2, points_arc_3, points_arc_4

