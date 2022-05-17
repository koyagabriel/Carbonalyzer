import { Layout, Tabs } from 'antd';
import PageHeaderComponent from "../components/PageHeader";
import Usage from "../components/Usage";
import styles from '../styles/Dashboard.module.css'

const Dashboard = () => {
  const { Header, Content} = Layout;
  const { TabPane } = Tabs;

  return(
    <Layout className={styles.layout}>
      <Header className={styles.header}>
        <PageHeaderComponent />
      </Header>
      <Content className={styles.content}>
        <Tabs type="card">
          <TabPane tab="Usages" key="1" className={styles.tabpane}>
            <Usage/>
          </TabPane>
          <TabPane tab="Usage Types" key="2" className={styles.tabpane}>
          </TabPane>
          <TabPane tab="Statistics" key="3" className={styles.tabpane}>
          </TabPane>
        </Tabs>
      </Content>
    </Layout>
  );
}

export default Dashboard;