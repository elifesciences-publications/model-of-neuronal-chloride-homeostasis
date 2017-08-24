# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 17:29:22 2016

@author: Kira
@title: Figure 4
"""
from plm_singlecomp_withkcc2 import plm, zp
from plotting import minifig, minithreefig, minifigtwoaxes,twoaxes,xcolor,clcolor,wcolor,kcolor
import matplotlib.pyplot as plt
from matplotlib import gridspec
from pylab import rcParams
import numpy as np
rcParams['figure.figsize'] = 8,8

sym=['-',':','--','-.']

def f4a(init_x=[40e-3,80e-3,120e-3,160e-3]):   
    plt.figure()
    for i in range(len(init_x)):
        endcl=plm(xinit=init_x[i],tt=240, k_init=0,osmofix=True)
        plt.subplot(2,1,1)
        plt.plot(endcl[11][1:-1],endcl[20][1:-1],'m'+sym[i])
        plt.subplot(2,1,2)
        plt.plot(endcl[11][0:-1],endcl[10][0:-1],'k'+sym[i])
    plt.savefig('f4a.eps')
    plt.show()
    print endcl[20][-1]
    
    return
    
def f4b(init_x=range(25,586,40)):
    endv=[]
    endk=[]
    endcl=[]
    endw =[]
    
    for i in init_x:
        end=plm(xinit=i*1e-3,k_init=0,tt=1000,osmofix=False)
        endv.append(end[9])
        endk.append(end[6])
        endcl.append(end[7])
        endw.append(end[21])
        print end[9]
        print end[6]
        print end[7]
    plt.figure()
    gs = gridspec.GridSpec(2, 1, height_ratios=[1.5, 1]) 
    a=plt.subplot(gs[0])
    a.plot(init_x,endcl,color=clcolor)
    a.plot(init_x,endcl,'bo')
    a.plot(init_x,endk,color=kcolor)
    a.plot(init_x,endk,'ro')
    a.plot(init_x,endv,'k')
    a.plot(init_x,endv,'ko')
    a.set_ylim([-100,-70])
    b=plt.subplot(gs[1])
    b.plot(init_x,endw,color=wcolor)
    b.plot(init_x,endw,'ko')
    b.set_ylim([0,8e-12])
    plt.savefig('f4b.eps')
    plt.show()
    
    return
    
def f4c(gX=1e-8,tt=540,xt=180,xend=180,xflux=4e-7):
    dex=plm(gx=gX,xt=xt,tt=tt,xflux=xflux,xend=xend)
    minithreefig([dex[11][1:-1],dex[14][1:-1],dex[13][1:-1],dex[16][1:-1],dex[10][1:-1],dex[20][1:-1]],xcolor,yl=[[-100,-70],[1.8e-12,3.3e-12],[154.5,158.5]])
    plt.savefig('f4c.eps')
    plt.show()
    print (dex[16][-1]-dex[14][-1])
    print (dex[16][8000]-dex[14][8000])
    return
    
def sf4c(GX=[5e-10,1e-9,5e-9,7e-9,1e-8,2e-8],tt=600,xt=25,ratio=0.98,xend=0):
    deltecl=[]
    maxdeltecl=[]
    deltw=[]
    deltx=[]
    for i in GX:
        dex=plm(gx=i,xt=xt,tt=tt,ratio=ratio,xend=xend)
        deltecl.append(dex[14][-1]-dex[14][1])
        maxdeltecl.append(max(np.absolute((dex[14]-dex[14][1]))))
        deltw.append((dex[10][-1])/dex[10][1])
        deltx.append(max(np.absolute((dex[20]-dex[20][1]))))
        minithreefig([dex[11][1:-1],dex[14][1:-1],dex[13][1:-1],dex[16][1:-1],dex[10][1:-1],dex[20][1:-1]],xcolor)
    print maxdeltecl
    twoaxes(GX,deltecl,maxdeltecl,deltx,deltw)
    return
    
def f4e(Z=range(-120,-50),moldelt=1e-12):
    molinit=plm(gx=1e-8,xt=25,tt=100,two=1,paratwo=True,moldelt=moldelt)
    zee=zp(Z=Z,molinit=molinit,moldelt=moldelt)
    newx=[]
    for i in zee[9]:
        newx.append(i)
    return zee[0],Z,zee,newx
    
def f4d(f=2e-3):
    dxe=plm(graph=1,gx=0,xt=120,two=0,tt=360,f4d=f)
    minithreefig([dxe[11][1:-1],dxe[14][1:-1],dxe[13][1:-1],dxe[16][1:-1],dxe[10][1:-1],dxe[23][1:-1]],xcolor,yl=[[-100,-70],[1.85e-12,2.0e-12],[0,0.12]])
    print (dxe[16][-1]-dxe[14][-1])
    print (dxe[16][8000]-dxe[14][8000])
    plt.savefig('f4d.eps')
    plt.show()
    return

def sf4fa():
    XF=[5e-14,1e-13,2e-13]
    GX=[-10,-9,-8]
    col=['mo','bo','go']
    plt.figure()
    for a in XF:
        for g in GX:
            dez=plm(tt=2500,moldelt=a,two=1,gx=10**g,xt=25,xend=0,ratio=0.8)
            #minithreefig([dez[11][1:-1],dez[14][1:-1],dez[13][1:-1],dez[16][1:-1],dez[10][1:-1],dez[22][1:-1]],'k')
            plt.plot(g,dez[22][-1],col[XF.index(a)])
    plt.show()
    return
    
def sf4fb():
    XF=[5e-14,1e-13,2e-13]
    rat=[0.2,0.4,0.6,0.8]
    GX=[-10,-9,-8]
    col=['mo','bo','go','ro']
    plt.figure()
    for s in XF:
        for r in rat:
            dez=plm(tt=500,moldelt=s,two=1,gx=10**(-8),xt=25,xend=0,ratio=r)
            #minithreefig([dez[11][1:-1],dez[14][1:-1],dez[13][1:-1],dez[16][1:-1],dez[10][1:-1],dez[22][1:-1]],'k')
            plt.plot(r,dez[22][-1],col[XF.index(s)])
            #plt.ylim((-0.83,-0.85))
    plt.show()
    return

def neww():
    a=plm(neww=1,ton=10,toff=90,tt=200)
    minithreefig([a[11][1:-1],a[14][1:-1],a[13][1:-1],a[16][1:-1],a[10][1:-1],a[20][1:-1]],xcolor)
    plt.show()
    return