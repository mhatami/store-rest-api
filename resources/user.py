
from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type= str,
        required = True,
        help="This field cannot be left blank"
    )
    parser.add_argument('password',
        type= str,
        required = True,
        help="This field cannot be left blank"
    )

    def post(self):
        data=UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message": "User already exists in DB."}, 400

        user = UserModel(data['username'], data['password'])
        user.save_to_db()

        return {"message": "User created successfully."}, 201
