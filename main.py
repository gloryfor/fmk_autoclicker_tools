import json
import math

src_resolution_x = 960
src_resolution_y = 540
dest_resolution_x = 1280
dest_resolution_y = 720

def main():
    with open('files/academy_gesture-pass_960x540.json', 'r') as file:
        data = json.load(file)
        for template in data:
            print(template['name'], end="\n")
            for target in template['targets']:
                old_target = target.copy()
                target['xPos'] = math.floor(target['xPos'] * dest_resolution_x / src_resolution_x)
                target['yPos'] = math.floor(target['yPos'] * dest_resolution_y / src_resolution_y)
                if target['xPos1'] > 0 and target['yPos1'] > 0:
                    target['xPos1'] = math.floor(target['xPos1'] * dest_resolution_x / src_resolution_x)
                    target['yPos1'] = math.floor(target['yPos1'] * dest_resolution_y / src_resolution_y)
                print(old_target, target, sep=' -> ', end='\n')

    with open('files/academy_gesture-pass_%sx%s.json' % (dest_resolution_x, dest_resolution_y), 'w', encoding='utf-8') as outfile:
        # json.dump(data, outfile, indent=2, ensure_ascii=False)
        json.dump(data, outfile, ensure_ascii=False)


if __name__ == '__main__':
    main()
