# Alan Chen
# Computer Vision Assignment
# Write a python script that does the following:
# For each cluter, the circle with the large area is kept,
# all other are removed. Return the resulting list of tuples

# Assumptions:
# - tuples in form of [(<float> x, <float> y, <float> r)]
# - each tuple has a unique radius

class overlapping_circles:
    # Creating global variables
    def __init__(self, tuples):
        self.tuples = tuples
        self.intersecting_circles = []

    # Adding the first set tuple into a the global list
    def check_overlapping(self):
        for i in range(0, len(self.tuples)):
            if self.intersecting_circles == []:
                self.intersecting_circles.append([self.tuples[i]])
            else:
                self.checkintersecting_circles(self.tuples[i])

    # Checks if incoming tuple intersect with any tuple in global list
    def checkintersecting_circles(self, tuple):
        # print(tuple)
        tuple_added = False
        for circles in self.intersecting_circles:
            inter_count = 0
            # print('CIRCLES', circles)
            # print('INTERCIRCLES', self.intersecting_circles)
            for i in range(0, len(circles)):
                # print('checking', circles[i], 'with', tuple)
                if self.checking_intersecting(circles[i], tuple):
                    inter_count += 1
            # print('count', inter_count)
            if inter_count > 0:
                circles.append(tuple)
                tuple_added = True
        if tuple_added is False:
            self.intersecting_circles.append([tuple])
        # print(self.intersecting_circles)

    # Returns True/False if they intersect
    def checking_intersecting(self, tup1, tup2):
        if (tup1[0] - tup2[0])**2 + (tup1[1] - tup2[1])**2 <= (tup1[2] + tup2[2])**2:
            return True
        else:
            return False

    # Goes into global list and finds largest in each cluster
    # Returns the largests one per cluster
    def find_largest_per_cluster_circle(self):
        largest_per_cluster = []
        for circles in self.intersecting_circles:
            # print('inner:',circles)
            big = circles[0]
            same_size_clusters = []
            for i in range(1,len(circles)):
                if circles[i][2] == big[2]:
                    same_size_clusters.append(circles[i])
                elif circles[i][2] > big[2]:
                    big = circles[i]
            if len(same_size_clusters) != 0:
                same_size_clusters.append(big)
                largest_per_cluster.append(same_size_clusters)
            else:
                largest_per_cluster.append([big])
        # for i in largest_per_cluster: print('returning largest_per_cluster:',i)
        return largest_per_cluster

if __name__ == '__main__':
    # tuples = [(1, 1, 1), (1, 1, 4), (1, 2, 4), (10, 10, 1), (6, 7, 1), (1, 4, 0.5)]
    tuples = [(1, 1, 1), (1, 1, 4), (7, 7, 2), (10, 10, 1), (6, 7, 1), (1, 4, 0.5)]
    oc = overlapping_circles(tuples)
    oc.check_overlapping()
    largest = oc.find_largest_per_cluster_circle()
    print('Given tupples:', tuples)
    print('The largest tuples in each cluster are:', largest)
