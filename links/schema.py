import graphene
import django_filters
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Link, Vote


class LinkFilter(django_filters.FilterSet):
    class Meta:
        model = Link
        fields = ["url", "description"]


class LinkNode(DjangoObjectType):
    class Meta:
        model = Link
        interfaces = (graphene.relay.Node,)


class VoteNode(DjangoObjectType):
    class Meta:
        model = Vote
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    link = graphene.relay.Node.Field(LinkNode)
    links = DjangoFilterConnectionField(LinkNode, filterset_class=LinkFilter)


class CreateLink(graphene.relay.ClientIDMutation):
    link = graphene.Field(LinkNode)

    class Input:
        url = graphene.String()
        description = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        user = info.context.user or None

        link = Link(
            url=input.get("url"), description=input.get("description"), posted_by=user,
        )
        link.save()

        return CreateLink(link=link)


class Mutation(graphene.AbstractType):
    relay_create_link = CreateLink.Field()
