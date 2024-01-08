import numpy as np
import scipy.special as sp




class Gaussian_Mode :
    def __init__(self, wavelength, w0):
        self.wavelength = wavelength
        self.w0 = w0
        self.ZR = np.pi*self.w0**2/self.wavelength
        self.k = 2*np.pi/self.wavelength

    def get_ZR(self):
        return np.pi*self.w0**2/self.wavelength
    
    def get_w(self, z):
        return self.w0*np.sqrt(1+(z/self.ZR)**2)
    
    def get_RZ(self, z):
        return z*(1+(self.ZR/z)**2)
    
    def get_phiZ(self, z):
        return np.arctan2(z,self.ZR)
    
    def get_field(self, r, z):
        w = self.get_w(z)
        Rz = self.get_RZ(z)
        phiZ = self.get_phiZ(z)
        term_1 = self.w0/w
        term_2 = np.exp(-r**2/w**2)
        term_3 = np.exp(-1j* ((self.k*r**2)/(2*Rz)+self.k*z-phiZ))
        return term_1*term_2*term_3
    
    def get_intensity(self, r, z):
        term_1 = (self.w0/self.get_w(z))**2
        term_2 = np.exp(-2*r**2/self.get_w(z)**2)
        return term_1*term_2



class LG_Mode :
    def __init__(self, p, l, wavelength, w0):
        self.p = p
        self.l = l
        self.wavelength = wavelength
        self.w0 = w0
        self.ZR = np.pi*self.w0**2/self.wavelength
        self.k = 2*np.pi/self.wavelength
        self.N = np.abs(self.l)+2*self.p
        self.C = np.sqrt(2*np.math.factorial(self.p)/(np.pi*np.math.factorial(self.p+np.abs(self.l))))

    def get_ZR(self):
        return np.pi*self.w0**2/self.wavelength
    
    def get_w(self, z):
        return self.w0*np.sqrt(1+(z/self.ZR)**2)
    
    def get_RZ(self, z):
        return z*(1+(self.ZR/z)**2)
    
    def get_phiZ(self, z):
        return (self.N+1)*np.arctan2(z,self.ZR)
    

    def get_field(self, r, z, phi):
        w = self.get_w(z)
        Rz = self.get_RZ(z)
        phiZ = self.get_phiZ(z)


        term_1 = self.C * (1/w) 
        term_2 = ((np.sqrt(2)*r/w)**np.abs(self.l))
        term_3 = np.exp(-r**2/w**2)
        term_4 = sp.genlaguerre(self.p,np.abs(self.l))(2*r**2/w**2)
        term_5 = np.exp(-1j*self.k*r**2/(2*Rz))
        term_6 = np.exp(-1j*self.l*phi)
        term_7 = np.exp(1j*phiZ)


        result = term_1*term_2*term_3*term_4*term_5*term_6*term_7

        return result
    
    def get_intensity(self, r, z):
        term_1 = 2*self.w0**2 *r**2/self.get_w(z)**4
        term_2 = np.exp(-2*r**2/self.get_w(z)**2)

        return term_1*term_2
      


    
