import graphene
import graphene_django_optimizer as gql_optimizer

from nautobot.extras.models import DynamicGroup
from nautobot.virtualization.models import VirtualMachine, VMInterface, Cluster
from nautobot.virtualization.filters import VirtualMachineFilterSet, VMInterfaceFilterSet, ClusterFilterSet


class ClusterType(gql_optimizer.OptimizedDjangoObjectType):
    """GraphQL type object for Cluster model."""

    dynamic_groups = graphene.List("nautobot.extras.graphql.types.DynamicGroupType")

    class Meta:
        model = Cluster
        filterset_class = ClusterFilterSet

    def resolve_dynamic_groups(self, args):
        return DynamicGroup.objects.get_for_object(self)


class VirtualMachineType(gql_optimizer.OptimizedDjangoObjectType):
    """GraphQL type object for VirtualMachine model."""

    dynamic_groups = graphene.List("nautobot.extras.graphql.types.DynamicGroupType")

    class Meta:
        model = VirtualMachine
        filterset_class = VirtualMachineFilterSet

    def resolve_dynamic_groups(self, args):
        return DynamicGroup.objects.get_for_object(self)


class VMInterfaceType(gql_optimizer.OptimizedDjangoObjectType):
    """GraphQL type object for VMInterface model."""

    class Meta:
        model = VMInterface
        filterset_class = VMInterfaceFilterSet
        exclude = ["_name"]

    # At the DB level, mac_address is null=False, but empty strings are represented as null in the ORM and REST API,
    # so for consistency, we'll keep that same representation in GraphQL.
    mac_address = graphene.String(required=False)
