import graphene


class Rating(graphene.ObjectType):
    rating_id = graphene.Int()
    user_id = graphene.String()
    destination_id = graphene.Int()
    rating = graphene.Float()
    review = graphene.String()


class AddRatingParams(graphene.InputObjectType):
    user_id = graphene.String()
    destination_id = graphene.Int()
    rating = graphene.Float()
    review = graphene.String()

class AddRatingResponse(graphene.Union):
    class Meta:
        types = (Rating,)

