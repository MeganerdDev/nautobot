import { RouterButton } from "./RouterButton";
import { ButtonGroup } from "@chakra-ui/react";
import * as Icon from "react-icons/tb";
import { useLocation } from "react-router-dom";
import {
    Box,
    Heading,
    NtcThumbnailIcon,
    MeatballsIcon,
    Button as UIButton,
    TableRenderer,
    useTableRenderer,
    createColumnHelper,
    PlusIcon,
} from "@nautobot/nautobot-ui";
import { useCallback, useMemo } from "react";

import NautobotTable from "@components/core/Table";
import Paginator from "@components/common/paginator";
import TableItem from "@components/core/TableItem";


const getTableItemLink = (idx, obj) => {
    if (idx === 0) {
        return window.location.pathname + obj.id;
    }
    if (typeof obj !== "object" || !obj || !obj.url) {
        return null;
    }
    // Remove domain + /api prefix
    const url = obj.url.replace(window.location.origin + "/api", "");

    // Statuses and Roles should not be linkable
    if(["/extras/statuses", "/extras/roles"].some(prefix => url.startsWith(prefix))) {
        return null;
    }
    return url;
}

// A composite component for displaying a object list table. Just the data!
export default function ObjectListTable({
    tableData,
    tableHeader,
    totalCount,
    active_page_number,
    page_size,
    gridColumn,
    tableTitle,
}) {
    let location = useLocation();
    const columnHelper = useMemo(() => createColumnHelper(), []);
    const columns = useMemo(
        () =>
        tableHeader.map(({ name, label }, idx) =>
                columnHelper.accessor(name, {
                    cell: (props) => {
                        // Get the column data from the object 
                        // e.g from {"status": {"display": "Active"}, "id": ....} get => {"display": "Active"}
                        const column_data = idx == 0 ? props.row.original : props.row.original[props.column.id]
                        return (
                            <TableItem
                                name={name}
                                obj={props.getValue()}
                                url={getTableItemLink(idx, column_data)}
                            />
                        )
                    },
                    header: label,
                })
            ),
        [columnHelper, tableHeader]
    );
    const onRowSelectionChange = useCallback(() => {
        // Do something.
    }, []);

    const table = useTableRenderer({
        columns: columns,
        data: tableData,
        enableMultiRowSelection: true,
        onRowSelectionChange,
    });

    return (
        <Box
            background="white-0"
            borderRadius="md"
            gridColumn={gridColumn}
            padding="md"
        >
            <div style={{display: "flex", justifyContent:"space-between", marginBottom: "20px"}}>
                <Heading 
                    as="h1" 
                    color="black-0" 
                    size="H1" 
                    style={{display: "flex", alignItems: "center", gap: "5px"}} 
                >
                    <NtcThumbnailIcon width="25px" height="30px" /> {tableTitle}
                </Heading>
                <ButtonGroup pb={2} style={{alignItems: "center"}}>
                    <UIButton size="sm" variant="secondary" > Filters </UIButton>
                    <UIButton size="sm" variant="primary" leftIcon={<MeatballsIcon />}> Actions </UIButton>
                    <Icon.TbMinusVertical />
                    <UIButton size="sm" leftIcon={<PlusIcon />}> Add {tableTitle} </UIButton>
                </ButtonGroup>
            </div>

            <TableRenderer table={table} />
            {/* <Paginator
                url={location.pathname}
                data_count={totalCount}
                page_size={page_size}
                active_page={active_page_number}
            ></Paginator> */}
        </Box>
    );
}
