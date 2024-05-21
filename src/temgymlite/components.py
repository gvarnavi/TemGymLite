import temgymlite.shapes as geom
import numpy as np

class Lens():
    '''Creates a lens component and handles calls to GUI creation, updates to GUI
        and stores the component matrix.
    '''    
    def __init__(self, z, name = '', f = 0.5, label_radius = 0.3, radius = 0.25, num_points = 50):
        '''

        Parameters
        ----------
        z : float
            Position of component in optic axis
        name : str, optional
            Name of this component which will be displayed by GUI, by default ''
        f : float, optional, 
            Focal length of this lens, by default 0.5
        label_radius : float, optional
            Location to place the label in the 3D GUI, by default 0.3
        radius : float, optional
            Radius of the 3D model of this component, by default 0.25
        num_points : int, optional
            Number of points to use to make the 3D model, by default 50
        '''        
        self.type = 'Lens'
        
        self.z = z
        self.radius = radius 
        self.label_radius = label_radius
        self.num_points = num_points
        
        self.f = f
        self.f_temp = f
        self.ftime = 0
        self.blocked_ray_idcs = []
        
        self.name = name
        self.set_matrix()
        
    def lens_matrix(self, f):
        '''Lens ray transfer matrix

        Parameters
        ----------
        f : float
            Focal length of lens

        Returns
        -------
        ndarray
            Output Ray Transfer Matrix
        '''        
        
        matrix = np.array([[1, 0,      0, 0, 0],
                           [-1 / f, 1,      0, 0, 0],
                           [0, 0,      1, 0, 0],
                           [0, 0, -1 / f, 1, 0],
                           [0, 0,       0, 0, 1]])

        return matrix
    
    def set_matrix(self): 

        '''
        '''        
        self.matrix = self.lens_matrix(self.f)
    
class AstigmaticLens():
    '''Creates an Astigmatic lens component and handles calls to GUI creation, updates to GUI
        and stores the component matrix.
    '''    
    def __init__(self, z, name = '', fx = -0.5, fy = -0.5, label_radius = 0.3, radius = 0.25, num_points = 50):
        '''

        Parameters
        ----------
        z : float
            Position of component in optic axis
        name : str, optional
            Name of this component which will be displayed by GUI, by default ''
        fx : float, optional, 
            Focal length of this lens in x, by default -0.5
        fx : float, optional, 
            Focal length of this lens in y, by default -0.5
        label_radius : float, optional
            Location to place the label in the 3D GUI, by default 0.3
        radius : float, optional
            Radius of the 3D model of this component, by default 0.25
        num_points : int, optional
            Number of points to use to make the 3D model, by default 50
        '''        

        self.type = 'Astigmatic Lens'
        self.z = z
        self.radius = radius 
        self.label_radius = label_radius
        self.num_points = num_points
        
        self.fx = fx
        self.fx_temp = fx
        self.fy = fy
        self.fy_temp = fy
        self.ftime = 0

        self.blocked_ray_idcs = []
        
        self.name = name
        
        self.set_matrix()
        
    def lens_matrix(self, fx, fy):
        '''Astigmatic lens ray transfer matrix

        Parameters
        ----------
        fx : float
            focal length in x
        fy : float
            focal length in y

        Returns
        -------
        ndarray
            Output Ray Transfer Matrix
        '''        
        
        matrix = np.array([[1, 0,      0, 0, 0],
                           [-1 / fx, 1,      0, 0, 0],
                           [0, 0,      1, 0, 0],
                           [0, 0, -1 / fy, 1, 0],
                           [0, 0,       0, 0, 1]])

        return matrix
    
    def set_matrix(self):
        '''
        '''        
        self.matrix = self.lens_matrix(self.fx, self.fy)
    
class Quadrupole():
    '''Creates a quadrupole component and handles calls to GUI creation, updates to GUI
        and stores the component matrix. Almost exactly the same as astigmatic lens component
        '''
    def __init__(self, z, name = '', fx = -0.5, fy = -0.5, label_radius = 0.3, radius = 0.25, num_points = 50):
        '''

        Parameters
        ----------
        z : float
            Position of component in optic axis
        name : str, optional
            Name of this component which will be displayed by GUI, by default ''
        fx : float, optional, 
            Focal length of this lens in x, by default -0.5
        fx : float, optional, 
            Focal length of this lens in y, by default -0.5
        label_radius : float, optional
            Location to place the label in the 3D GUI, by default 0.3
        radius : float, optional
            Radius of the 3D model of this component, by default 0.25
        num_points : int, optional
            Number of points to use to make the 3D model, by default 50
        '''        

        self.type = 'Quadrupole'
        self.z = z
        self.radius = radius 
        self.label_radius = label_radius
        self.num_points = num_points
        
        self.fx = fx
        self.fx_temp = fx
        self.fy = fy
        self.fy_temp = fy
        self.ftime = 0

        self.blocked_ray_idcs = []
        
        self.name = name
        
        self.set_matrix()
        
    def lens_matrix(self, fx, fy):
        '''Quadrupole lens ray transfer matrix

        Parameters
        ----------
        fx : float
            focal length in x
        fy : float
            focal length in y

        Returns
        -------
        ndarray
            Output Ray Transfer Matrix
        '''        
        
        matrix = np.array([[1, 0,      0, 0, 0],
                           [-1 / fx, 1,      0, 0, 0],
                           [0, 0,      1, 0, 0],
                           [0, 0, -1 / fy, 1, 0],
                           [0, 0,       0, 0, 1]])

        return matrix
    
    def set_matrix(self):
        '''
        '''        
        self.matrix = self.lens_matrix(self.fx, self.fy)
    
class Deflector():
    '''Creates a single deflector component and handles calls to GUI creation, updates to GUI
        and stores the component matrix. See Double Deflector component for a more useful version
    '''    
    def __init__(self, z, name = '', defx = 0.5, defy = 0.5, label_radius = 0.3, radius = 0.25, num_points = 50):
        '''_summary_

        Parameters
        ----------
        z : float
            Position of component in optic axis
        name : str, optional
            Name of this component which will be displayed by GUI, by default ''
        defx : float, optional
            deflection kick in slope units to the incoming ray x angle, by default 0.5
        defy : float, optional
            deflection kick in slope units to the incoming ray y angle, by default 0.5
        label_radius : float, optional
            Location to place the label in the 3D GUI, by default 0.3
        radius : float, optional
            Radius of the 3D model of this component, by default 0.25
        num_points : int, optional
            Number of points to use to make the 3D model, by default 50
        '''         
        self.type = 'Deflector'
        
        self.z = z
        self.radius = radius 
        self.label_radius = label_radius
        self.num_points = num_points
        
        self.defx = defx
        self.defy = defy
        self.defx_temp = defx
        self.defy_temp = defy
        
        self.blocked_ray_idcs = []
        
        self.name = name
        
        self.set_matrix()
        
    def deflector_matrix(self, def_x, def_y):
        '''Single deflector ray transfer matrix

        Parameters
        ----------
        def_x : float
            deflection in x in slope units
        def_y : _type_
            deflection in y in slope units

        Returns
        -------
        ndarray
            Output ray transfer matrix
        '''        
        
        matrix = np.array([[1, 0, 0, 0,          0],
                           [0, 1, 0, 0, def_x],
                           [0, 0, 1, 0,          0],
                           [0, 0, 0, 1, def_y],
                           [0, 0, 0, 0,         1]])

        return matrix
    
    def set_matrix(self): 
        '''
        '''        
        self.matrix = self.deflector_matrix(self.defx, self.defy)
    
        
class DoubleDeflector():
    '''Creates a double deflector component and handles calls to GUI creation, updates to GUI
        and stores the component matrix. Primarily used in the Beam Tilt/Shift alignment.
    '''    
    def __init__(self, z_up, z_low, name = '', updefx = 0.0, updefy = 0.0, lowdefx = 0.0, lowdefy = 0.0, 
                 scan_rotation = 0, label_radius = 0.3, radius = 0.25, num_points = 50):
        '''

        Parameters
        ----------
        z_up : float
            Position of the upper deflection component in optic axis
        z_low : float
            Position of the lower deflection component in optic axis
        name : str, optional
            Name of this component which will be displayed by GUI, by default ''
        updefx : float, optional
            deflection kick of upper deflector
            in slope units to the incoming ray x angle,
            by default 0.0
        updefy : float, optional
            deflection kick of upper deflector
            in slope units to the incoming ray y angle,
            by default 0.0
        lowdefx : float, optional
            deflection kick of lower deflector
            in slope units to the incoming ray x angle,
            by default 0.0
        lowdefy : float, optional
            deflection kick of lower deflector
            in slope units to the incoming ray y angle,
            by default 0.0
        label_radius : float, optional
            Location to place the label in the 3D GUI, by default 0.3
        radius : float, optional
            Radius of the 3D model of this component, by default 0.25
        num_points : int, optional
            Number of points to use to make the 3D model, by default 50
        '''        

        self.type = 'Double Deflector'
        
        self.z_up = z_up
        self.z_low = z_low
        self.dist = self.z_up - z_low
        self.radius = radius
        self.label_radius = label_radius
        self.num_points = num_points
        
        self.updefx = updefx
        self.updefy = updefy
        
        self.lowdefx = lowdefx
        self.lowdefy = lowdefy
        
        self.updefx_temp = updefx
        self.updefy_temp = updefy
        
        self.lowdefx_temp = lowdefx
        self.lowdefy_temp = lowdefy
        
        self.defratiox_temp = -1.
        self.defratioy_temp = -1.
        
        self.scan_rotation = scan_rotation
        
        self.defratiox = -1.
        self.defratioy = -1.
        
        self.name = name
        self.blocked_ray_idcs = []
        
        self.set_matrices()
        
        self.xtime = 0
        self.ytime = 0
        
    def deflector_matrix(self, def_x, def_y):
        '''Single deflector ray transfer matrix

        Parameters
        ----------
        def_x : float
            deflection in x in slope units
        def_y : _type_
            deflection in y in slope units

        Returns
        -------
        ndarray
            Output ray transfer matrix
        '''        
        matrix = np.array([[1, 0, 0, 0,          0],
                           [0, 1, 0, 0, def_x],
                           [0, 0, 1, 0,          0],
                           [0, 0, 0, 1, def_y],
                           [0, 0, 0, 0,         1]])

        return matrix
    
    def rotation_matrix(self, scan_rotation):
        '''Scan rotation ray transfer matrix

        Parameters
        ----------
        scan_rotation : float
            scan_rotation in degrees

        Returns
        -------
        ndarray
            Output ray transfer matrix
        '''        
        rad = (scan_rotation/180)*np.pi
        matrix = np.array([[np.cos(rad), 0, -np.sin(rad), 0, 0],
                           [0, 1, 0, 0, 0],
                           [np.sin(rad), 0, np.cos(rad), 0, 0],
                           [0, 0, 0, 1, 0],
                           [0, 0, 0, 0, 1]])

        return matrix
        
    
    def set_matrices(self):
        '''
        '''        
        self.up_matrix = self.deflector_matrix(self.updefx, self.updefy)
        self.low_matrix = np.matmul(self.rotation_matrix(self.scan_rotation), self.deflector_matrix(self.lowdefx, self.lowdefy))#self.deflector_matrix(self.lowdefx, self.lowdefy)
    
class Biprism():
    '''Creates a biprism component and handles calls to GUI creation, updates to GUI and stores the component
    parameters. Important to note that the transfer matrix of the biprism is only cosmetic: It still
    need to be multiplied by the sign of the position of the ray to perform like a biprism. 
    '''    
    def __init__(self, z, name = '', deflection = 0.5, theta = 0, label_radius = 0.3, radius = 0.25, width = 0.01, num_points = 50):
        '''

        Parameters
        ----------
        z : float
            Position of component in optic axis
        name : str, optional
            Name of this component which will be displayed by GUI, by default ''
        deflection : float, optional
            Biprism deflection kick in slope units to the incoming ray angle, by default 0.5
        theta: int, optional
            Angle of the biprism - Two options - 0 or 1. 0 for 0 degree rotation, 1 for 90 degree rotation, by default 0
        label_radius : float, optional
            Location to place the label in the 3D GUI, by default 0.3
        radius : float, optional
            Radius of the 3D model of this component, by default 0.25
        width : float, optional
            Width of the biprism model, by default 0.01
        num_points : int, optional
            Number of points to use to make the 3D model, by default 50
        '''        
        self.type = 'Biprism'
        
        self.z = z
        self.theta = theta
        self.radius = radius 
        self.label_radius = label_radius
        self.num_points = num_points
        self.width = width
        
        self.deflection = deflection
        self.blocked_ray_idcs = []
        self.name = name
        
        self.set_matrix()
        
    def biprism_matrix(self, deflection):
        '''Biprims deflection matrix - only used to store values. 

        Parameters
        ----------
        deflection : float
            update deflection kick to rays in slope coordinates

        Returns
        -------
        ndarray
            Output transfer matrix
        '''        
        matrix = np.array([[1, 0, 0, 0, 0],
                           [0, 1, 0, 0, deflection*np.sin(self.theta)],
                           [0, 0, 1, 0, 0],
                           [0, 0, 0, 1, deflection*np.cos(self.theta)],
                           [0, 0, 0, 0, 1]])

        return matrix
    
    def set_matrix(self):
        '''
        '''        
        self.matrix = self.biprism_matrix(self.deflection)
    
class Aperture():
    '''Creates an aperture component and handles calls to GUI creation, updates to GUI and stores the component
    parameters. Important to note that the transfer matrix of the aperture only propagates rays. The logic of 
    blocking rays is handled inside the "model" function. 
    '''

    def __init__(self, z, name = 'Aperture', aperture_radius_inner = 0.005, aperture_radius_outer = 0.25, label_radius = 0.3, num_points = 50, x = 0, y = 0):
        '''

        Parameters
        ----------
        z : float
            Position of component in optic axis
        name : str, optional
            Name of this component which will be displayed by GUI, by default 'Aperture'
        aperture_radius_inner : float, optional
           Inner radius of the aperture, by default 0.005
        aperture_radius_outer : float, optional
            Outer radius of the aperture, by default 0.25
        label_radius : float, optional
            Location to place the label in the 3D GUI, by default 0.3
        num_points : int, optional
            Number of points to use to make the 3D model, by default 50
        x : int, optional
            X position of the centre of the aperture, by default 0
        y : int, optional
            Y position of the centre of the aperture, by default 0
        '''        

        self.type = 'Aperture'
        
        self.name = name
        
        self.x = x
        self.y = y
        self.z = z

        self.aperture_radius_inner = aperture_radius_inner
        self.aperture_radius_outer = aperture_radius_outer
        self.min_radius = self.aperture_radius_inner
        self.max_radius = 0.90*self.aperture_radius_outer
        
        self.label_radius = label_radius
        self.num_points = num_points
        
        self.set_matrix()
        
        self.blocked_ray_idcs = []
        
    def set_matrix(self):
        '''
        '''        
        self.matrix = self.aperture_matrix
    
    def aperture_matrix(self):
        '''Aperture transfer matrix - simply a unit matrix of ones because 
        we only need to propagate rays that pass through the centre of the aperture. 

        Returns
        -------
        ndarray
            unit matrix
        '''        
        #creates a placeholder aperture matrix
        matrix = np.array([[1, 0, 0, 0, 0],
                           [0, 1, 0, 0, 0],
                           [0, 0, 1, 0, 0],
                           [0, 0, 0, 1, 0],
                           [0, 0, 0, 0, 1]])

        return matrix
    
