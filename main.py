import json
import random

# Python is actually braindead and needs these false defintions it doesn't even follow
# or else it'll fucking explode for no reason
true = True
false = False

# Number of asteroids
Num = 100
# Number through cycle
i = 0
for i in range(0, Num):
    Name = "Asteroid_" + str(i)

    # Other Parameters
    semiMajorAxis = random.randint(2800, 3600)
    inclination = random.randint(-5, 5)
    trueAnomaly = 360 * (i/Num)

    size = random.randint(1000, 2000)

    # Make the Data
    data = {
        "$schema": "https://raw.githubusercontent.com/xen-42/outer-wilds-new-horizons/main/NewHorizons/Schemas/body_schema.json",
        "name": Name,
        "starSystem": "2walker2.OogaBooga",
        "Base": {
            "gravityFallOff": "linear",
            "invulnerableToSun": true,
            "surfaceGravity": 10.0,
            "surfaceSize": 0.02 * size
        },
        "Atmosphere": {
            "hasOxygen": true,
            "hasTrees": true,
            "useAtmosphereShader": false,
            "fogDensity": 0.05,
            "fogTint": {
                "r": 227,
                "g": 79,
                "b": 202,
                "a": 255
            },
            "fogSize": 200
        },
        "canShowOnTitle": false,
        "Orbit": {
            "primaryBody": "Spark",
            "isMoon": true,
            "showOrbitLine": false,
            "semiMajorAxis": semiMajorAxis,
            "inclination": inclination,
            "trueAnomaly": trueAnomaly
        },
        "Props": {
            "details": [
                {
                    "assetBundle": "planets/Assets/turtle.evacring",
                    "path": "Assets/Dogshit/Evac/Ring_stuff/rock.00" + str(random.randint(1, 9)) + ".prefab",
                    "position": {},
                    "rotation": {
					    "x": random.randint(0, 359),
					    "y": random.randint(0, 359),
					    "z": random.randint(0, 359)
				    },
                    "scale": size,
                    "keepLoaded": true
                }
            ],
            "scatter": [
                {
                    "assetBundle": "planets/Assets/turtle.evacring",
                    "path": "Assets/Dogshit/Evac/Ring_stuff/Mushroom.prefab",
                    "keepLoaded": true,
                    "count": random.randint(0, 5),
                    "scale": (random.randint(30, 100)/1000),
                    "seed": random.randint(0, 1000)
                }
            ]
        },
        "ReferenceFrame": {
            "enabled": true,
            "hideInMap": false
        }
    }

    # Make/Write File
    with open('Output/' + Name + '.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    i = i + 1
