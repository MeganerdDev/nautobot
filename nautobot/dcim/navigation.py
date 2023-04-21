from nautobot.core.apps import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuImportButton, NavMenuTab


menu_items = (
    NavMenuTab(
        name="Organization",
        weight=100,
        groups=(
            NavMenuGroup(
                name="Locations",
                weight=150,
                items=(
                    NavMenuItem(
                        link="dcim:locationtype_list",
                        name="Location Types",
                        weight=100,
                        permissions=[
                            "dcim.view_locationtype",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="dcim:locationtype_add",
                                permissions=[
                                    "dcim.add_locationtype",
                                ],
                            ),
                            NavMenuImportButton(
                                link="dcim:locationtype_import",
                                permissions=[
                                    "dcim.add_locationtype",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="dcim:location_list",
                        name="Locations",
                        weight=200,
                        permissions=[
                            "dcim.view_location",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="dcim:location_add",
                                permissions=[
                                    "dcim.add_location",
                                ],
                            ),
                            NavMenuImportButton(
                                link="dcim:location_import",
                                permissions=[
                                    "dcim.add_location",
                                ],
                            ),
                        ),
                    ),
                ),
            ),
            NavMenuGroup(
                name="Racks",
                weight=200,
                items=(
                    NavMenuItem(
                        link="dcim:rack_list",
                        name="Racks",
                        weight=100,
                        permissions=[
                            "dcim.view_rack",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="dcim:rack_add",
                                permissions=[
                                    "dcim.add_rack",
                                ],
                            ),
                            NavMenuImportButton(
                                link="dcim:rack_import",
                                permissions=[
                                    "dcim.add_rack",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="dcim:rackgroup_list",
                        name="Rack Groups",
                        weight=200,
                        permissions=[
                            "dcim.view_rackgroup",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="dcim:rackgroup_add",
                                permissions=[
                                    "dcim.add_rackgroup",
                                ],
                            ),
                            NavMenuImportButton(
                                link="dcim:rackgroup_import",
                                permissions=[
                                    "dcim.add_rackgroup",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="dcim:rackreservation_list",
                        name="Reservations",
                        weight=400,
                        permissions=[
                            "dcim.view_rackreservation",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="dcim:rackreservation_add",
                                permissions=[
                                    "dcim.add_rackreservation",
                                ],
                            ),
                            NavMenuImportButton(
                                link="dcim:rackreservation_import",
                                permissions=[
                                    "dcim.add_rackreservation",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="dcim:rack_elevation_list",
                        name="Elevations",
                        weight=500,
                        permissions=[
                            "dcim.view_rack",
                        ],
                        buttons=(),
                    ),
                ),
            ),
        ),
    ),
    NavMenuTab(
        name="Devices",
        weight=200,
        groups=(
            NavMenuGroup(
                name="Devices",
                weight=100,
                items=(
                    NavMenuItem(
                        link="dcim:device_list",
                        name="Devices",
                        weight=100,
                        permissions=[
                            "dcim.view_device",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="dcim:device_add",
                                permissions=[
                                    "dcim.add_device",
                                ],
                            ),
                            NavMenuImportButton(
                                link="dcim:device_import",
                                permissions=[
                                    "dcim.add_device",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="dcim:platform_list",
                        name="Platforms",
                        weight=300,
                        permissions=[
                            "dcim.view_platform",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="dcim:platform_add",
                                permissions=[
                                    "dcim.add_platform",
                                ],
                            ),
                            NavMenuImportButton(
                                link="dcim:platform_import",
                                permissions=[
                                    "dcim.add_platform",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="dcim:virtualchassis_list",
                        name="Virtual Chassis",
                        weight=400,
                        permissions=[
                            "dcim.view_virtualchassis",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="dcim:virtualchassis_add",
                                permissions=[
                                    "dcim.add_virtualchassis",
                                ],
                            ),
                            NavMenuImportButton(
                                link="dcim:virtualchassis_import",
                                permissions=[
                                    "dcim.add_virtualchassis",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="dcim:deviceredundancygroup_list",
                        name="Device Redundancy Groups",
                        weight=500,
                        permissions=[
                            "dcim.view_deviceredundancygroup",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="dcim:deviceredundancygroup_add",
                                permissions=[
                                    "dcim.add_deviceredundancygroup",
                                ],
                            ),
                            NavMenuImportButton(
                                link="dcim:deviceredundancygroup_import",
                                permissions=[
                                    "dcim.add_deviceredundancygroup",
                                ],
                            ),
                        ),
                    ),
                ),
            ),
            NavMenuGroup(
                name="Device Types",
                weight=200,
                items=(
                    NavMenuItem(
                        link="dcim:devicetype_list",
                        name="Device Types",
                        weight=100,
                        permissions=[
                            "dcim.view_devicetype",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="dcim:devicetype_add",
                                permissions=[
                                    "dcim.add_devicetype",
                                ],
                            ),
                            NavMenuImportButton(
                                link="dcim:devicetype_import",
                                permissions=[
                                    "dcim.add_devicetype",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="dcim:manufacturer_list",
                        name="Manufacturers",
                        weight=200,
                        permissions=[
                            "dcim.view_manufacturer",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="dcim:manufacturer_add",
                                permissions=[
                                    "dcim.add_manufacturer",
                                ],
                            ),
                            NavMenuImportButton(
                                link="dcim:manufacturer_import",
                                permissions=[
                                    "dcim.add_manufacturer",
                                ],
                            ),
                        ),
                    ),
                ),
            ),
            NavMenuGroup(
                name="Connections",
                weight=300,
                items=(
                    NavMenuItem(
                        link="dcim:cable_list",
                        name="Cables",
                        weight=100,
                        permissions=[
                            "dcim.view_cable",
                        ],
                        buttons=(
                            NavMenuImportButton(
                                link="dcim:cable_import",
                                permissions=[
                                    "dcim.add_cable",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="dcim:console_connections_list",
                        name="Console Connections",
                        weight=200,
                        permissions=[
                            "dcim.view_consoleport",
                            "dcim.view_consoleserverport",
                        ],
                        buttons=(),
                    ),
                    NavMenuItem(
                        link="dcim:power_connections_list",
                        name="Power Connections",
                        weight=300,
                        permissions=[
                            "dcim.view_powerport",
                            "dcim.view_poweroutlet",
                        ],
                        buttons=(),
                    ),
                    NavMenuItem(
                        link="dcim:interface_connections_list",
                        name="Interface Connections",
                        weight=400,
                        permissions=[
                            "dcim.view_interface",
                        ],
                        buttons=(),
                    ),
                ),
            ),
            NavMenuGroup(
                name="Device Components",
                weight=400,
                items=(
                    NavMenuItem(
                        link="dcim:interface_list",
                        name="Interfaces",
                        weight=100,
                        permissions=[
                            "dcim.view_interface",
                        ],
                        buttons=(
                            NavMenuImportButton(
                                link="dcim:interface_import",
                                permissions=[
                                    "dcim.add_interface",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="dcim:frontport_list",
                        name="Front Ports",
                        weight=200,
                        permissions=[
                            "dcim.view_frontport",
                        ],
                        buttons=(
                            NavMenuImportButton(
                                link="dcim:frontport_import",
                                permissions=[
                                    "dcim.add_frontport",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="dcim:rearport_list",
                        name="Rear Ports",
                        weight=300,
                        permissions=[
                            "dcim.view_rearport",
                        ],
                        buttons=(
                            NavMenuImportButton(
                                link="dcim:rearport_import",
                                permissions=[
                                    "dcim.add_rearport",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="dcim:consoleport_list",
                        name="Console Ports",
                        weight=400,
                        permissions=[
                            "dcim.view_consoleport",
                        ],
                        buttons=(
                            NavMenuImportButton(
                                link="dcim:consoleport_import",
                                permissions=[
                                    "dcim.add_consoleport",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="dcim:consoleserverport_list",
                        name="Console Server Ports",
                        weight=500,
                        permissions=[
                            "dcim.view_consoleserverport",
                        ],
                        buttons=(
                            NavMenuImportButton(
                                link="dcim:consoleserverport_import",
                                permissions=[
                                    "dcim.add_consoleserverport",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="dcim:powerport_list",
                        name="Power Ports",
                        weight=600,
                        permissions=[
                            "dcim.view_powerport",
                        ],
                        buttons=(
                            NavMenuImportButton(
                                link="dcim:powerport_import",
                                permissions=[
                                    "dcim.add_powerport",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="dcim:poweroutlet_list",
                        name="Power Outlets",
                        weight=700,
                        permissions=[
                            "dcim.view_poweroutlet",
                        ],
                        buttons=(
                            NavMenuImportButton(
                                link="dcim:poweroutlet_import",
                                permissions=[
                                    "dcim.add_poweroutlet",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="dcim:devicebay_list",
                        name="Device Bays",
                        weight=800,
                        permissions=[
                            "dcim.view_devicebay",
                        ],
                        buttons=(
                            NavMenuImportButton(
                                link="dcim:devicebay_import",
                                permissions=[
                                    "dcim.add_devicebay",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="dcim:inventoryitem_list",
                        name="Inventory Items",
                        weight=900,
                        permissions=[
                            "dcim.view_inventoryitem",
                        ],
                        buttons=(
                            NavMenuImportButton(
                                link="dcim:inventoryitem_import",
                                permissions=[
                                    "dcim.add_inventoryitem",
                                ],
                            ),
                        ),
                    ),
                ),
            ),
        ),
    ),
    NavMenuTab(
        name="Power",
        weight=600,
        groups=(
            NavMenuGroup(
                name="Power",
                weight=100,
                items=(
                    NavMenuItem(
                        link="dcim:powerfeed_list",
                        name="Power Feeds",
                        permissions=[
                            "dcim.view_powerfeed",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="dcim:powerfeed_add",
                                permissions=[
                                    "dcim.add_powerfeed",
                                ],
                            ),
                            NavMenuImportButton(
                                link="dcim:powerfeed_import",
                                permissions=[
                                    "dcim.add_powerfeed",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="dcim:powerpanel_list",
                        name="Power Panels",
                        permissions=[
                            "dcim.view_powerpanel",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="dcim:powerpanel_add",
                                permissions=[
                                    "dcim.add_powerpanel",
                                ],
                            ),
                            NavMenuImportButton(
                                link="dcim:powerpanel_import",
                                permissions=[
                                    "dcim.add_powerpanel",
                                ],
                            ),
                        ),
                    ),
                ),
            ),
        ),
    ),
)
