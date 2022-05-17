import { Table, Tag, Space } from 'antd';
import { useState } from "react";
import useSWR from "swr";
import { useAxiosApi } from "../lib/hooks";
import { getUsages } from "../lib/api";

const columns = [
  {
    title: 'Amount',
    dataIndex: 'amount',
    key: 'amount',
  },
  {
    title: 'Usage At',
    dataIndex: 'usage_at',
    key: 'usage_at',
  },
  {
    title: 'Usage type',
    dataIndex: 'usage_type',
    key: 'usage_type',
  }
];

const Usage = () => {
  const [usages, setUsages] = useState({});
  const [page, setPage] = useState(1)
  const axiosApi = useAxiosApi();
  const onSuccessHandler = (data) => {
    setUsages(data);
    setPage(null);
  };
  const handlePageChange = (page, pageSize) => { setPage(page) };
  useSWR(page ? [axiosApi, page] : null, getUsages, {
    onSuccess: onSuccessHandler
  });
  const data = usages.results;
  return (
    <Table
      columns={columns}
      dataSource={data}
      pagination={{
        showSizeChanger: false,
        pageSize: 100,
        onChange: handlePageChange,
        showTotal: (total) => `Total ${total} items`,
        total: usages.count
      }}
    />
  );
};

export default Usage;