from pico2d import *

#관리 모듈

#게임 월드의 표현
#두개의 layer를 갖는 게임월드로 구현
objects=[[],[]]
def add_object(o,depth=0):
    objects[depth].append(o)

#월드 업뎃, 객체 업뎃
def update():
    for layer in objects:
      for o in layer:
        o.update()

#월드 객체들을 모두 그리기
def render():
    for layer in objects:
      for o in layer:
        o.draw()

#객체 삭제
def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            return 
    raise ValueError('object none')