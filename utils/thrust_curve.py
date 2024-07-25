

class ThrustCurve:
    def __init__(self, path) -> None:
        f = open(path)
        lines = f.readlines()
        no_comments = filter(lambda x: not x.startswith(';'), lines)
        no_header = list(no_comments)[1:]
        pairs = list(map(lambda x: x.split(), no_header))
        pairs_numbers = list(map(lambda x: [float(x[0]),float(x[1])], pairs))
        pairs_numbers.insert(0, [0.0,0.0])
        self.data = pairs_numbers

    # get how much the current thrust is based on time since ignition
    def get_thrust(self, t):
        if t <= 0.0 or t > self.data[-1][0]:
            return 0.0
        
        start = [0,0]
        end = self.data[-1]
        for idx, x in enumerate(self.data):
            if x[0] >= t:
                end = x
                if(idx > 0):
                    start = self.data[idx -1]
                else:
                    start = [0.0, 0.0]
                break
        
        print(start[0])
        print(end[0])
        slope = (end[1] - start[1]) / (end[0] - start[0])
        offset = start[1] - (slope * start[0])

        return (slope * t) + offset

if __name__ == "__main__":
    tc = ThrustCurve("./rocket-trajectory-2/config/thrust_curve/Estes_C6.eng")
    print(tc.get_thrust(0.014))
            