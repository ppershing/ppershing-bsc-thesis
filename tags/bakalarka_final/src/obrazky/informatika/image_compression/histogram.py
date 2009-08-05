class Histogram:
    def MakeHistogramImage(data, N, H, norm):
        mmin = min(data)
        mmax = max(data)
        count = [0 for i in range(N)]

        for i in data:
            count[ int((i / (mmax-mmin) - mmin) * (N-1)) ]+=1.0/len(data)

        image_data = [[ 0 for i in range(N)] for j in range(H)]
        for i in range(N):
            image_data[0][i] = 1
            image_data[H-1][i] = 1
            
        for i in range(H):
            image_data[i][0] = 1
            image_data[i][N-1] = 1

        print count

        for i in range(N):
            for j in range(int(count[i]*norm*(H-1))):
                image_data[H-1-j][i]=1

        return image_data
    MakeHistogramImage = staticmethod(MakeHistogramImage)
