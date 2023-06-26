import React from "react";
import { Text, Select } from "@nautobot/nautobot-ui";
import { Flex } from "@chakra-ui/react";
import { useSearchParams } from "react-router-dom";

export default function PaginatorForm({ start, end, total_count, scroll_ref }) {
    let [searchParams, setSearchParams] = useSearchParams();
    function onPageSizeChange(event) {
        let offset = searchParams.get("offset");
        // Scroll to the top of the ObjectListTable Container on table reload
        scroll_ref.current.scrollIntoView({
            alignToTop: true,
            behavior: "smooth",
        });
        setSearchParams({
            limit: event.target.value,
            offset: offset ? offset : 0,
        });
    }

    return (
        <Flex align="center">
            <Text color="gray-3" pr="sm">Show</Text>
            <Select
                value={
                    searchParams.get("limit") ? searchParams.get("limit") : "50"
                }
                onChange={onPageSizeChange}
            >
                {/*
                    TODO: we need a REST API endpoint to query get_settings_or_config("PER_PAGE_DEFAULTS")
                    rather than hard-coding this.
                */}
                <option value="10">10</option>
                <option value="25">25</option>
                <option value="50">50</option>
                <option value="100">100</option>
                <option value="200">200</option>
                <option value="500">500</option>
            </Select>
            <Text color="gray-3" pl="sm" whiteSpace="nowrap">rows per page</Text>
        </Flex>
    );
}
