import {
    AutomationIcon,
    DcimIcon,
    IpamIcon,
    NautobotGridItem,
    PlatformIcon,
    SecurityIcon,
    Table,
    TableContainer,
    Tab,
    Tabs,
    TabList,
    TabPanel,
    TabPanels,
    Tag,
    TagLabel,
    Tbody,
    Td,
    Text,
    Th,
    Thead,
    Tr,
} from "@nautobot/nautobot-ui";
import HomeChangelogPanel from "@components/HomeChangelogPanel";
import HomePanel from "@components/HomePanel";
import JobHistoryTable from "@components/JobHistoryTable";
import { LoadingWidget } from "@components/LoadingWidget";
import { useGetObjectCountsQuery, useGetRESTAPIQuery } from "@utils/api";
import GenericView from "@views/generic/GenericView";

export default function Home() {
    const { data: jobResultData } = useGetRESTAPIQuery({
        app_name: "extras",
        model_name: "job-results",
        limit: 1,
        depth: 0,
    });
    const {
        data: objectCountData,
        isLoading,
        isError,
    } = useGetObjectCountsQuery();

    if (isLoading) {
        return (
            <GenericView>
                <LoadingWidget />
            </GenericView>
        );
    }

    if (isError) {
        return (
            <GenericView>
                <Text>Error loading.</Text>
            </GenericView>
        );
    }

    return (
        <GenericView columns="1 1 1 1 3 1" gridBackground="white-0">
            <HomePanel
                icon=<DcimIcon />
                title="Inventory"
                data={objectCountData["Inventory"]}
            />
            <HomePanel
                icon=<IpamIcon />
                title="Networks"
                data={objectCountData["Networks"]}
            />
            {/*TODO: this should use objectCountData["Security"]*/}
            <HomePanel
                icon=<SecurityIcon />
                title="Security"
                data={[
                    { name: "Menu Item 1", count: 0 },
                    { name: "Menu Item 2", count: 0 },
                    { name: "Menu Item 3", count: 0 },
                    { name: "Menu Item 4", count: 0 },
                    { name: "Menu Item 5", count: 0 },
                    { name: "Menu Item 6", count: 0 },
                ]}
            />
            <HomePanel
                icon=<PlatformIcon />
                title="Platform"
                data={objectCountData["Platform"]}
            />
            <NautobotGridItem colSpan="3">
                {/*TODO: this should probably be extracted to a HomeAutomationPanel component for readability?*/}
                <TableContainer>
                    <Table>
                        <Thead>
                            <Tr _hover={{}}>
                                <Th width="3em">
                                    <AutomationIcon />
                                </Th>
                                <Th>Automation</Th>
                            </Tr>
                        </Thead>
                        <Tbody>
                            <Tr _hover={{}}>
                                <Td colspan={2}>
                                    <Tabs variant="outline">
                                        <TabList>
                                            <Tab>
                                                Job History{" "}
                                                <Tag size="sm" variant="info">
                                                    <TagLabel>
                                                        {jobResultData?.count}
                                                    </TagLabel>
                                                </Tag>
                                            </Tab>
                                            <Tab>
                                                Schedule{" "}
                                                <Tag size="sm" variant="info">
                                                    <TagLabel>7</TagLabel>
                                                </Tag>
                                            </Tab>
                                            <Tab>
                                                Approvals{" "}
                                                <Tag size="sm" variant="info">
                                                    <TagLabel>3</TagLabel>
                                                </Tag>
                                            </Tab>
                                        </TabList>
                                        <TabPanels>
                                            <TabPanel>
                                                <JobHistoryTable />
                                            </TabPanel>
                                            <TabPanel></TabPanel>
                                            <TabPanel></TabPanel>
                                        </TabPanels>
                                    </Tabs>
                                </Td>
                            </Tr>
                        </Tbody>
                    </Table>
                </TableContainer>
            </NautobotGridItem>
            <HomeChangelogPanel />
        </GenericView>
    );
}
