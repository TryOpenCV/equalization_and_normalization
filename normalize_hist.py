import cv2
import cv

def compute_histogram(src, h_bins = 30, s_bins = 32, scale = 10):
    '''calculate histogram from picture'''
    #create images
    hsv = cv.CreateImage(cv.GetSize(src), 8, 3)
    hplane = cv.CreateImage(cv.GetSize(src), 8, 1)
    splane = cv.CreateImage(cv.GetSize(src), 8, 1)
    vplane = cv.CreateImage(cv.GetSize(src), 8, 1)

    planes = [hplane, splane]
    cv.CvtColor(src, hsv, cv.CV_BGR2HSV)
    cv.CvtPixToPlane(hsv, hplane, splane, vplane, None)

    #compute histogram
    hist = cv.CreateHist((h_bins, s_bins), cv.CV_HIST_ARRAY,
            ranges = ((0, 180),(0, 255)), uniform = True)
    cv.CalcHist(planes, hist)      #compute histogram
    cv.NormalizeHist(hist, 1.0)    #normalize histo

    return hist

def show_histogram(hist, hbins = 30, sbins = 32, scale = 10):
    #create image to use to visualize our histogram
    hist_img = cv.CreateImage((hbins*scale, sbins*scale), 8, 3)
    cv.Zero(hist_img)

    #populate our visualization with little squares
    vals = cv.GetMinMaxHistValue(hist)
    print "histogram vals: ",vals
    #TODO: try to vectorise this computation <-- python "for" is expensive
    for h in range(0, hbins):
        for s in range(0, sbins):
            bin_val = cv.QueryHistValue_2D(hist, h, s)
            intensity = cv.Round(bin_val * 255.0 / vals[1])
            p1 = (h * scale, s * scale)
            p2 = ((h-1)* scale, (s-1) * scale)
            color = cv.RGB(intensity, intensity, intensity)
            cv.Rectangle(hist_img, p1, p2, color, cv.CV_FILLED)

    #show image
    cv.ShowImage("H-S histogram", hist_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

src = cv.LoadImage("donkey.png", cv.CV_LOAD_IMAGE_COLOR)
hist1 = compute_histogram(src)
h_bins = 30
s_bins = 32
scale = 10
show_histogram(hist1, h_bins, s_bins, scale)
