from flask_restx import Namespace,Resource,fields
from ..models.orders import Order
from ..models.users import User
from http import HTTPStatus
from flask_jwt_extended import jwt_required,get_jwt_identity

order_namespace = Namespace('orders', description="a namespace for orders")

order_model =order_namespace.model(
    'Order',{
        'id':fields.Integer(description = 'An ID'),
        'size':fields.String(description = 'Size of order',required = True, enum = ['SMALL','MEDIUM','LARGE','EXTRA-LARGE']),
        'order_status':fields.String(description = 'Status of the order',required = True, enum = ['PENDING','IN_TRANSIT','DELIVERED']),
        #'flavor':fields.String(description = 'Flavor of the order',required = True),
        #'quantity':fields.Integer(description = 'Amount of orders',required = True )      
        
    }
)
@order_namespace.route('/orders')
class OrderGetCreate(Resource):
    
    @order_namespace.marshal_with(order_model)
    @jwt_required()
    
    def get(self):
        """
            Get all orders
        """
        orders= Order.query.all()
        
        return orders,HTTPStatus.OK
    
    @order_namespace.expect(order_model)
    @order_namespace.marshal_with(order_model)
    @jwt_required()
    def post(self):
        """
            Place a new order
        """
        
        username = get_jwt_identity()
        
        current_user=User.query.filter_by(username=username).first()
        data = order_namespace.payload
        
        new_order = Order(
            size = data['size'],
            quantity = data['quantity'],
            flavor = data['flavor']
        )
        
        new_order.user = current_user
        
        new_order.save()
        
        return new_order,HTTPStatus.CREATED
    
@order_namespace.route('/order/<int:order_id>')
class GetUpdateDelete(Resource):
    
    def get(self,order_id):
        """
            Retrieve an order by ID
        """
        pass
    
    def put(self,order_id):
        """
            Update an order by ID
        """
        pass
    
    def delete(self,order_id):
        """
            Delete an order by ID
        """
        pass
    
@order_namespace.route('/user/<int:user_id>/order/<int:order_id>')
class GetSpecificOrderByUser(Resource):
    def get(self,user_id,order_id):
        """
            Get a user's specific order
        """
        pass
    
@order_namespace.route('/user/<int:user_id>/orders')
class UserOrders(Resource):
    def get(self,user_id):
        """
            Get all orders by a specific user
        """
        pass
    
@order_namespace.route('/order/status/<int:order_id>')
class UpdateOrderStatus(Resource):
    def patch(self,order_id):
        """
            Update an order's status
        """
        pass