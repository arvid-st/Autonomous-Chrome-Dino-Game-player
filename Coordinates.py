import pyautogui as pag
# All coordinates are taken on 1920x1080 resolution

screenWidth, screenHeight = pag.size()

AbsoluteCoordinateScoreTopLeft = (1219, 316)
AbsoluteCoordinateScoreBottomRight = (1219, 316)
RelativeCoordinateScoreTopLeft = (AbsoluteCoordinateScoreTopLeft[0] / 1920 * screenWidth, AbsoluteCoordinateScoreTopLeft[1] / 1080 * screenHeight)
RelativeCoordinateScoreBottomRight = (AbsoluteCoordinateScoreBottomRight[0] / 1920 * screenWidth + 53, AbsoluteCoordinateScoreBottomRight[1] / 1080 * screenHeight + 11)
RelativeCoordinateScore = (RelativeCoordinateScoreTopLeft, RelativeCoordinateScoreBottomRight)

AbsoluteCoordinateObstacleTopLeft = (1190, 387)
# (979,316) (1032, 327) same coordinates but on 1440x1080. still 53 pixels in width even with 4:3 ration instead of 16:9
# 979 / 1440 = 0.67986111111. 1219 / 1920 =  0.63489583333
AbsoluteCoordinateObstacleBottomRight = (1290, 465)
RelativeCoordinateObstacleTopLeft = (AbsoluteCoordinateObstacleTopLeft[0] / 1920 * screenWidth, AbsoluteCoordinateObstacleTopLeft[1] / 1080 * screenHeight)
RelativeCoordinateObstacleBottomRight = (AbsoluteCoordinateObstacleBottomRight[0] / 1920 * screenWidth, AbsoluteCoordinateObstacleBottomRight[1] / 1080 * screenHeight)
RelativeCoordinateObstacle = (RelativeCoordinateObstacleTopLeft, RelativeCoordinateObstacleBottomRight)

# All score images have the same height of 316 -> 327 (10 pixels)

# Entire score capture: 1219 -> 1272 (53 pixels) with 4x gaps with 2 pixels.

# Each image is there for (53 - 4x2) / 5 pixels in width. (53-4x2) / 2 = 9
# Each image is 9 pixels in width, 10 pixels high

# All points bellow are only x-coordinate since y-coordinate is the same for all score numbers

# 10 000 score place: 1219 -> 1219 + 9 (1228)
# 1 000 score place: 1228 + 2 (1230) -> 1230 + 9 (1239)
# 100 score place: 1239 + 2 (1241) -> 1241 + 9 (1250)
# 10 score place: 1250 + 2 (1252) -> 1252 + 9 (1261)
# 1 score place: 1261 + 2 (1263) -> 1263 + 9 (1272)

AbsoluteCoordinateTenThousandScoreTopLeft = (1219, 316)
AbsoluteCoordinateTenThousandScoreBottomRight = (1219, 316)
RelativeCoordinateTenThousandScoreTopLeft = (AbsoluteCoordinateTenThousandScoreTopLeft[0] / 1920 * screenWidth, AbsoluteCoordinateTenThousandScoreTopLeft[1] / 1080 * screenHeight)
RelativeCoordinateTenThousandScoreBottomRight = (AbsoluteCoordinateTenThousandScoreBottomRight[0] / 1920 * screenWidth + 9, AbsoluteCoordinateTenThousandScoreBottomRight[1] / 1080 * screenHeight + 11)
RelativeCoordinateTenThousandScore = (RelativeCoordinateTenThousandScoreTopLeft, RelativeCoordinateTenThousandScoreBottomRight)

AbsoluteCoordinateThousandScoreTopLeft = (1230, 316)
AbsoluteCoordinateThousandScoreBottomRight = (1230, 316)
RelativeCoordinateThousandScoreTopLeft = (AbsoluteCoordinateThousandScoreTopLeft[0] / 1920 * screenWidth, AbsoluteCoordinateThousandScoreTopLeft[1] / 1080 * screenHeight)
RelativeCoordinateThousandScoreBottomRight = (AbsoluteCoordinateThousandScoreBottomRight[0] / 1920 * screenWidth + 9, AbsoluteCoordinateThousandScoreBottomRight[1] / 1080 * screenHeight + 11)
RelativeCoordinateThousandScore = (RelativeCoordinateThousandScoreTopLeft, RelativeCoordinateThousandScoreBottomRight)

AbsoluteCoordinateHundredScoreTopLeft = (1241, 316)
AbsoluteCoordinateHundredScoreBottomRight = (1241, 316)
RelativeCoordinateHundredScoreTopLeft = (AbsoluteCoordinateHundredScoreTopLeft[0] / 1920 * screenWidth, AbsoluteCoordinateHundredScoreTopLeft[1] / 1080 * screenHeight)
RelativeCoordinateHundredScoreBottomRight = (AbsoluteCoordinateHundredScoreBottomRight[0] / 1920 * screenWidth + 9, AbsoluteCoordinateHundredScoreBottomRight[1] / 1080 * screenHeight + 11)
RelativeCoordinateHundredScore = (RelativeCoordinateHundredScoreTopLeft, RelativeCoordinateHundredScoreBottomRight)

AbsoluteCoordinateTenScoreTopLeft = (1252, 316)
AbsoluteCoordinateTenScoreBottomRight = (1252, 316)
RelativeCoordinateTenScoreTopLeft = (AbsoluteCoordinateTenScoreTopLeft[0] / 1920 * screenWidth, AbsoluteCoordinateTenScoreTopLeft[1] / 1080 * screenHeight)
RelativeCoordinateTenScoreBottomRight = (AbsoluteCoordinateTenScoreBottomRight[0] / 1920 * screenWidth + 9, AbsoluteCoordinateTenScoreBottomRight[1] / 1080 * screenHeight + 11)
RelativeCoordinateTenScore = (RelativeCoordinateTenScoreTopLeft, RelativeCoordinateTenScoreBottomRight)

AbsoluteCoordinateOneScoreTopLeft = (1263, 316)
AbsoluteCoordinateOneScoreBottomRight = (1263, 316)
RelativeCoordinateOneScoreTopLeft = (AbsoluteCoordinateOneScoreTopLeft[0] / 1920 * screenWidth, AbsoluteCoordinateOneScoreTopLeft[1] / 1080 * screenHeight)
RelativeCoordinateOneScoreBottomRight = (AbsoluteCoordinateOneScoreBottomRight[0] / 1920 * screenWidth + 9, AbsoluteCoordinateOneScoreBottomRight[1] / 1080 * screenHeight + 11)
RelativeCoordinateOneScore = (RelativeCoordinateOneScoreTopLeft, RelativeCoordinateOneScoreBottomRight)