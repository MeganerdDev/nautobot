import { Card, Tab, Table, Tabs } from "react-bootstrap"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faCheck, faMinus, faXmark } from "@fortawesome/free-solid-svg-icons"
import { useParams } from "react-router-dom"
import useSWR from "swr"

import create_plugin_tab from "@components/plugins/PluginTab"
import PluginComponents from "@components/core/Plugins"
import PluginFullWidthComponentsWithProps from "@components/plugins/PluginFullWidthComponents"
import { nautobot_url } from "src/index"


const fetcher = (url) => fetch(url, { credentials: "include" }).then((res) => res.ok ? res.json() : null)
const fetcherHTML = (url) => fetch(url, { credentials: "include" }).then((res) => res.ok ? res.text() : null)
const fetcherTabs = (url) => fetch(url, { credentials: "include" }).then((res) => {
  return res.json().then((data) => {

    let tabs = []
    data.tabs.map((tab_top) => {
      Object.keys(tab_top).map(function (tab_key) {
        let tab = tab_top[tab_key]
        let tab_component = create_plugin_tab({ tab: tab })
        tabs.push(tab_component)
      })
    })
    return tabs
  })
})

function render_value(value) {
  switch (typeof value) {
    case "object":
      return value === null ? <FontAwesomeIcon icon={faMinus} /> : Array.isArray(value) ? <ul></ul> : value["display"]
    case "boolean":
      return value ? <FontAwesomeIcon icon={faCheck} /> : <FontAwesomeIcon icon={faXmark} />
    default:
      return value === "" ? <FontAwesomeIcon icon={faMinus} /> : value
  }
}

function RenderRow(props) {
  var key = props.identifier;
  var value = props.value;

  if (["id", "url", "display", "slug", "notes_url"].includes(key) ^ !!props.advanced) {
    return null;
  }

  if (key[0] === "_") return null

  // "foo_bar" --> "Foo Bar"
  key = key.split("_").map((x) => (x ? x[0].toUpperCase() + x.slice(1) : "")).join(" ");

  return (
    <tr>
      <td>{key}</td>
      <td>{render_value(value)}</td>
    </tr>
  );
}

export default function ObjectRetrieve({ api_url }) {
  var pluginConfig = []
  const { app_name, model_name, object_id } = useParams()
  if (!!app_name && !!model_name && !!object_id && !api_url) {
    api_url = `${nautobot_url}/api/${app_name}/${model_name}/${object_id}/`
  }
  const { data: objectData, error } = useSWR(() => api_url, fetcher)
  const { data: pluginHTML } = useSWR(() => api_url ? api_url + "plugin_full_width_fragment/" : null, fetcherHTML)
  const ui_url = objectData ? `${nautobot_url}${objectData.formData.web_url}?viewconfig=true` : null
  var { data: pluginConfig } = useSWR(() => ui_url, fetcherTabs)
  if (error) return <div>Failed to load {api_url}</div>
  if (!objectData) return <></>
  if (!pluginConfig) return <></>

  const route_name = `${app_name}:${model_name}`;

  let obj = objectData.formData

  const default_view = (<>
    <h1>{obj.name}</h1>
    <p>
      <small className="text-muted">
        {obj.created &&
          <>Created {obj.created} &middot; </>
        }
        <> Updated <span title={obj.last_updated}>xyz seconds</span> ago</>
      </small>
    </p>
    <div className="pull-right noprint"></div>
    <Tabs defaultActiveKey="main" mountOnEnter={true}>
      <Tab key="main" eventKey="main" title="Main">
        <br />
        <Card>
          <Card.Header>
            <strong>Main</strong>
          </Card.Header>
          <Table hover>
            <tbody>
              {Object.keys(obj).map((key, idx) => <RenderRow identifier={key} value={obj[key]} advanced={false} key={idx} />)}
            </tbody>
          </Table>
        </Card>
        <br />
        <div dangerouslySetInnerHTML={{ __html: pluginHTML }} />
        <br />
        {PluginFullWidthComponentsWithProps(route_name, obj)}
      </Tab>
      <Tab key="advanced" eventKey="advanced" title="Advanced">
        <br />
        <Card>
          <Card.Header>
            <strong>Advanced</strong>
          </Card.Header>
          <Table hover>
            <tbody>
              {Object.keys(obj).map((key, idx) => <RenderRow identifier={key} value={obj[key]} advanced key={idx} />)}
            </tbody>
          </Table>
        </Card>
      </Tab>
      <Tab key="notes" eventKey="notes" title="Notes">
        Notes to be rendered here.
      </Tab>
      <Tab key="change_log" eventKey="change_log" title="Change Log">
        <p>Changelog to be rendered here</p>
      </Tab>
      {pluginConfig}
    </Tabs>
  </>)

  let return_view = default_view;
  if (PluginComponents.CustomViews?.[route_name] && "retrieve" in PluginComponents.CustomViews?.[route_name]) {
    const CustomView = PluginComponents.CustomViews[route_name].retrieve
    return_view = <CustomView {...obj} />
  }

  return return_view
}