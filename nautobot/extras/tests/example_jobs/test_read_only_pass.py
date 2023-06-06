from nautobot.dcim.models import Location, LocationType
from nautobot.extras.jobs import Job
from nautobot.extras.models import Status


class TestReadOnlyPass(Job):
    """
    Ready only Job with pass result.
    """

    description = "Validate job import"

    class Meta:
        read_only = True

    def run(self, data, commit):
        """
        Job function.
        """
        location_type = LocationType.objects.create(name="Job Root Type")
        status = Status.objects.get_for_model(Location).first()
        location = Location.objects.create(name="New Location", location_type=location_type, status=status)

        self.log_success(obj=location)