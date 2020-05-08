from collections import deque
#rows=int(input('enter no of rows'));
#cols=int(input(('enter no of columns')));

rows,cols=0,0
start,end=0,0
points=""
infectedpatients_location=[]

import random
import flask,json
from flask import request,jsonify
from json import dumps,dump,loads


value =''
app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route("/post/values",methods=["POST"])
def set_values():
    if not request.json:
        global rows,cols,start,end,points,infectedpatients_location
        rows,cols=10,10
        start=1
        end=3
        points="(0,0)"
        infectedpatients_location=[]
    dic ={}
    rows= int(request.json.get('rows'))
    dic["rows"] = rows
    cols = int(request.json.get('cols'))
    dic["cols"] = cols
    start = int(request.json.get('start'))
    dic["start"] = start
    end = int(request.json.get('end'))
    dic["end"] = end
    points = request.json.get('points')
    import re
    z = re.findall("[0-9]+", points)
    for i in range(0, len(z), 2):
        infectedpatients_location.append((int(z[i]), int(z[i + 1])))
    dic["points"] = infectedpatients_location

    print(dic.items());
    #dump_string = dumps(dic)
    #json_data = loads(dump_string)
    response = app.response_class(
        response=json.dumps(dic),
        status=200,
        mimetype='application/json'
    )
    print('response', response)
    return response;

@app.route("/get_final_infected",methods=["GET"])
def calculate_display():
    matrix = [[0 for j in range(cols)] for i in range(rows)];
    antibody=[]
    for i in range(rows):
        x,y=random.randint(0,rows-1),random.randint(0,cols-1);
        antibody.append([x,y]);


    for x,y in antibody:
        matrix[x][y]='A';

    #infectedpatients_location=[[1,1],[5,5],[7,8]]


    queue=deque();
    for x,y in infectedpatients_location:
        matrix[x][y] = 1;
        queue.append((x,y,0));
    infectedpatients=len(queue);
    starttime=start;
    startpatientcount=0
    endpatientcount=0;
    endtime=end;
    while(queue):
        x,y,time=queue.popleft();
        if(time==starttime):
            startpatientcount=infectedpatients;
        if(time==endtime):
            endpatientcount=infectedpatients;
            break;

        adjacent= [[1,0],[-1,0],[0,1],[0,-1],[-1,-1],[-1,1],[1,1],[1,-1]] # eight adjacents left,right,top bottom and corners -4
        loc1, loc2 = random.randint(0, 7), random.randint(0,7); # picking 2 people among 8 adjacent people
        for dx,dy in [adjacent[loc1],adjacent[loc2]]:
            if(0<=x+dx<rows and 0<=y+dy<cols ):
                if(matrix[x+dx][y+dy]==0):
                    matrix[x+dx][y+dy]=1;
                    infectedpatients+=1;
                    queue.append((x+dx,y+dy,time+1));
    dic = {}
    dic["matrix"] = matrix
    dic["startpatientcount"]=startpatientcount
    dic["endpatientcount"]=endpatientcount
    dic["infected_patients"] = endpatientcount - startpatientcount
    #return str(matrix);
    #return value
    #print(startpatientcount,endpatientcount)
    #print(endpatientcount- startpatientcount);
    return dumps(dic)
if __name__ == "__main__":
    app.run(host ='127.0.0.1',port=5010,debug=True)
