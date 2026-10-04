from flask import Blueprint,jsonify,request
from app.models.labor_model import LaborsModels
from app.extentions import db 
labor_bp = Blueprint(
    "labors",
    __name__
)

@labor_bp.post('/labors')
def create():
    data=request.get_json()
    labor_ = LaborsModels(
        name=data['name'],
        email=data['email']
    )
    db.session.add(labor_)
    db.session.commit()
    return jsonify({
        'status':'labor added',
        'data':labor_.to_dict()
    }),201 

@labor_bp.get('/labors')
def getalllabors():
    labors = LaborsModels.query.all()
    print(labors)
    return jsonify(
        [labor.to_dict() for labor in labors]
    )

@labor_bp.get('/labors/<int:id>')
def getalllaborsid(id):
    labor_ = db.session.get(LaborsModels,id)
    if not labor_:
        return jsonify({
            'status':'labor not found against this id'
        })
    return jsonify(labor_.to_dict())

@labor_bp.put('/labors/<int:id>')
def getalllaborsupdateid(id):
    labor_ = db.session.get(LaborsModels,id)
    data=request.get_json()
    if not labor_:
        return jsonify({
            'status':'labor not found against this id'
        })
    labor_.name=data['name']
    labor_.email=data['email']

    db.session.commit()
    return jsonify({
        'status':'labor updated',
        'data':labor_.to_dict()})

@labor_bp.delete('/labors/<int:id>')
def delete(id):
    labor_ = db.session.get(LaborsModels,id)
    if not labor_:
        return jsonify({
            'status':'labor not found against this id'
        })
    db.session.delete(labor_)
    db.session.commit()
    return jsonify({
            'status':'labor deleted'})