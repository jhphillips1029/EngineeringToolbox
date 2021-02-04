import matplotlib.pyplot as plt
import numpy as np

class Deltoid:
    def __init__(self,a,b,o,color=None):
        self.a = a * 0.5
        self.b = b * 0.5 * 0.75**0.5
        self.o = o
        self.color = color
        self.tags = {}
    
    def __str__(self):
        return "Left-most corner: ({:.4f}, {:.4f})\nOrientation: {:.0f}".format(self.a,self.b,self.o)
    
    def coord(self):
        a = self.a
        b = self.b
        o = self.o
        
        rtn = [[a,a+0.5,a+1,a],
               [b,b+o*0.75**0.5,b,b]]
        
        return rtn
    
    def plot(self,axis=None,color=None):
        if axis == None:
            axis = plt.gca()
        if color == None:
            color = self.color
        
        axis.plot(self.coord()[0],self.coord()[1],'k')
        axis.fill_between(self.coord()[0],min(self.coord()[1]),self.coord()[1],facecolor=color)
        
        axis.set_aspect('equal', adjustable='box')
        
    def coord_rect(self):
        shape = self.coord()
        
        k = 3**0.5
        theta = np.radians(-45)

        R = [[np.cos(-theta),-np.sin(-theta)],
             [np.sin(-theta), np.cos(-theta)]]
        T = [[1,0],[0,1/k]]

        new_shape = [[],[]]
        for x,y in zip(shape[0],shape[1]):
            v = np.array([[x],[y]])
            B = np.matmul(R,np.matmul(T,v))
            new_shape[0].append(B[0][0])
            new_shape[1].append(B[1][0])
            
        return new_shape
            
    def plot_rect(self,axis=None,color=None):
        if axis == None:
            axis = plt.gca()
        if color == None:
            color = self.color
        
        axis.plot(self.coord_rect()[0],self.coord_rect()[1],'k')
        axis.fill_between(self.coord_rect()[0],min(self.coord_rect()[1]),self.coord_rect()[1],facecolor=color)
        
        axis.set_aspect('equal', adjustable='box')
        
    def center(self):
        return [self.a+0.5,self.b+self.o*3**0.5/6]
    
    def mark(self,tag,value):##
        self.tags[tag] = value
        
def determine_adjacencies(cluster,allow_repeat=False):
    deltas = list(range(len(cluster)))
    adjacencies = []
    
    distance = lambda x1,y1,x2,y2: ( (x2-x1)**2 + (y2-y1)**2 )**0.5
    
    for d1 in deltas:
        start = d1+1
        ads = []
        if allow_repeat:
            start = 0
        for d2 in range(start,len(cluster)):
            if d2 == d1:
                continue
            c1 = cluster[d1].center()
            c2 = cluster[d2].center()
            if distance(c1[0],c1[1],c2[0],c2[1]) < 2/3 * 3**0.5 - 0.15:
                ads.append(d2)
                
        adjacencies.append(ads)
        
    return {delta:ad for delta,ad in zip(deltas,adjacencies)}

def shared_perimeter(d1,d2,return_points=False):
    d1_x = d1.coord()[0]
    d1_y = d1.coord()[1]
    d2_x = d2.coord()[0]
    d2_y = d2.coord()[1]
    for lst in [d1_x,d1_y,d2_x,d2_y]:
        lst.pop()
        
    num_decimal_pts = 8
    pts_1 = [(round(x,num_decimal_pts),round(y,num_decimal_pts)) for x,y in zip(d1_x,d1_y)]
    pts_2 = [(round(x,num_decimal_pts),round(y,num_decimal_pts)) for x,y in zip(d2_x,d2_y)]
    pts = []
    
    dups = 0
    for i in pts_1:
        if i in pts_2:
            dups+=1
            pts.append(i)
            
    distance = lambda x1,y1,x2,y2: ( (x2-x1)**2 + (y2-y1)**2 )**0.5
            
    if dups == 2:
        if return_points:
            return [2*distance(pts[0][0],pts[0][1],pts[1][0],pts[1][1]),list(pts[0]),list(pts[1])]
        else:
            return 2*distance(pts[0][0],pts[0][1],pts[1][0],pts[1][1])
    
    pts = []
    for pt in pts_1:
        if distance(pt[0],pt[1],d2.center()[0],d2.center()[1]) < 1/3+0.1:
            pts.append(pt)
            
    for pt in pts_2:
        if distance(pt[0],pt[1],d1.center()[0],d1.center()[1]) < 1/3+0.1:
            pts.append(pt)
            
    if len(pts) == 1:
        if return_points:
            return [0,list(pts[0]),list(pts[0])]
        return 0
    
    if len(pts) == 0:
        if return_points:
            return [0,list(pts_1[0]),list(pts_1[0])]
        return 0
        
    d = distance(pts[0][0],pts[0][1],pts[1][0],pts[1][1])
    
    if return_points:
        return [2*d,list(pts[0]),list(pts[1])]
    return 2*d

def find_red_deltas(cluster):
    indices = []
    for i in range(len(cluster)):
        delta = cluster[i]
        if delta.color == 'r' or delta.color == 'Red':
            indices.append(i)
            
    return indices

def get_centers(cluster):
    centers = []
    for delta in cluster:
        centers.append(delta.center())
        
    return centers

def centroid(cluster):
    centers = []
    for delta in cluster:
        centers.append(delta.center())
        
    A_0 = 0.5*1*(3**0.5/2)
    
    S_A = len(cluster) * A_0
    S_xA = 0
    S_yA = 0
    
    for center in centers:
        S_xA += A_0*center[0]
        S_yA += A_0*center[1]
        
    x_bar = S_xA/S_A
    y_bar = S_yA/S_A
    
    return [x_bar,y_bar]

def plot_cluster(cluster,ignore_deltas=False,centers=False,com=False,indices=False,bounding=False,ioi=-1,ioi_furthest_point=False,furthest_points=False,furthest_point_method="com",axis=None,nc_weight=1.0):
    if axis == None:
        axis = plt.gca()
    
    conv = 0.15
    for delta in cluster:
        if not ignore_deltas:
            c = None
            if cluster.index(delta) == ioi:
                c = 'y'
            delta.plot(color = c,axis=axis)
        if centers:
            axis.plot(delta.center()[0],delta.center()[1],'ko')
        if indices:
            cen = 0.4
            if cluster.index(delta) < 10:
                cen = 0.5
            axis.text(delta.a+cen-conv,delta.b+delta.o*3**0.5/6-conv,"{}".format(cluster.index(delta)))
        if bounding:
            axis.add_patch(plt.Circle(tuple(delta.center()),3**0.5/3,color=delta.color,fill=False))
        if furthest_points:
            far_point = get_furthest_point(cluster,cluster.index(delta),furthest_point_method,nc_weight)
            axis.plot(far_point[0],far_point[1],'mo')
            
    if com:
        cluster_centroid = centroid(cluster)
        axis.plot(cluster_centroid[0],cluster_centroid[1],'go')
        
    if ioi > -1 and ioi_furthest_point:
        ioi_furthest = get_furthest_point(cluster,ioi,furthest_point_method)
        axis.plot(ioi_furthest[0],ioi_furthest[1],'mo')
        
def mark_radiators(cluster,string):
    if len(cluster) != len(string):
        raise ValueError("Length of string and cluster must be equal!")
        
    for tag,delta in zip(string,cluster):
        delta.mark("radiative_vertex",tag)
        
def radiative_length(cluster,delta):
    connections = determine_adjacencies(cluster,True)
    d1 = cluster.index(delta)
    tol = 1.0e-5
    rad_tag = delta.tags["radiative_vertex"]
    d_x = delta.coord()[0]
    d_y = delta.coord()[1]
    d_x.pop()
    d_y.pop()
    
    p_rad = []
    if rad_tag == "o":
        return 0
    elif rad_tag == "l":
        p_rad.append(d_x[0])
        p_rad.append(d_y[0])
    elif rad_tag == "c":
        p_rad.append(d_x[1])
        p_rad.append(d_y[1])
    elif rad_tag == "r":
        p_rad.append(d_x[2])
        p_rad.append(d_y[2])
    else:
        inp = float(input("Unknown tag '{}'. Please provide length:".format(rad_tag)))
        return inp
    
    remaining = [[],[]]
    # Get other two points
    for x,y in zip(d_x,d_y):
        if x == p_rad[0] and y == p_rad[1]:
            continue
        remaining[0].append(x)
        remaining[1].append(y)
    
    radiate_length = 0
    
    # Determine if points on adjacent deltas lie along line connection other two nodes
    adjacent_deltas = connections[d1]
    to_r1 = lambda x: (remaining[1][0]-p_rad[1])/(remaining[0][0]-p_rad[0]) * (x-p_rad[0]) + p_rad[1]
    to_r2 = lambda x: (remaining[1][1]-p_rad[1])/(remaining[0][1]-p_rad[0]) * (x-p_rad[0]) + p_rad[1]
    distance = lambda x1,y1,x2,y2: ( (x2-x1)**2 + (y2-y1)**2 )**0.5
    
    #check if anything on side 1
    #print("Checking Side 1...")
    points_on_side_1 = []
    for d_i in adjacent_deltas:
        coords = cluster[d_i].coord()
        d_x = coords[0]
        d_x.pop()
        d_y = coords[1]
        d_y.pop()
        
        for x,y in zip(d_x,d_y):
            if y <= to_r1(x)+tol and y >= to_r1(x)-tol:
                #print("Point located on side 1!")
                points_on_side_1.append([x,y])
                
    if len(points_on_side_1) > 0:
        radiate_length += min([distance(point[0],point[1],p_rad[0],p_rad[1]) for point in points_on_side_1])
    elif len(points_on_side_1) == 0:
        radiate_length += 1
                
    #check if anything on side 2
    #print("Checking Side 2...")
    points_on_side_2 = []
    for d_i in adjacent_deltas:
        coords = cluster[d_i].coord()
        d_x = coords[0]
        d_x.pop()
        d_y = coords[1]
        d_y.pop()
        
        for x,y in zip(d_x,d_y):
            if y <= to_r2(x)+tol and y >= to_r2(x)-tol:
                #print("Point located on side 2!")
                points_on_side_2.append([x,y])
                
    blocked_node = True
    for point in points_on_side_2:
        blocked_node = blocked_node and distance(point[0],point[1],p_rad[0],p_rad[1]) <= 1
    
    if len(points_on_side_2) > 0:
        radiate_length += min([distance(point[0],point[1],p_rad[0],p_rad[1]) for point in points_on_side_2])
    elif len(points_on_side_2) == 0:
        radiate_length += 1
    
    return 2*radiate_length

def get_longest_chain(seed,modulize=True):
    chain = []
    chain.append(seed)
    i = 0
    while True:
        adj = new_connections[chain[i]]

        if len(adj) < 1:
            break

        if len(adj) == 1:
            lst = shared_perimeter(cluster[chain[i]],cluster[adj[0]],True)
            pts = lst[1:]
            if pts[0][1] == pts[1][1] and modulize:
                break
            chain.append(adj[0])
            i += 1

        if len(adj) > 1:
            old_adj = adj.copy()
            adj = []
            for j in old_adj:
                lst = shared_perimeter(cluster[chain[i]],cluster[j],True)
                pts = lst[1:]
                if pts[0][1] == pts[1][1] and modulize:
                    continue
                adj.append(j)
                
            lengths = [len(get_longest_chain(i)) for i in adj]
            chain.append(adj[lengths.index(max(lengths))])
            i += 1

    return chain

def get_deltan_distances(p1,p2):
    x_shared = 1/(2*3**0.5) * ( 3**0.5*(p2[0]+p1[0]) + p2[1]-p1[1] )
    p2_new = p2.copy()
    p2_new[0] += 1.0e-5
    y_shared = (p2[1]-p1[1])/(p2_new[0]-p1[0]) * (x_shared-p1[0]) + p1[1]
    distance = lambda x1,y1,x2,y2: ( (x2-x1)**2 + (y2-y1)**2 )**0.5

    x_ab = x_shared
    y_ab = y_shared
    d_y = 2*distance(p1[0],p1[1],x_ab,y_ab)
    d_x = 2*distance(p2[0],p2[1],x_ab,y_ab)

    if p1[0] > p2[0]:
        d_y *= -1
    if p1[1] < p2[1]:
        d_x *= -1
        
    return [d_x,d_y]
