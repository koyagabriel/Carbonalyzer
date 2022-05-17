import { useState, useContext } from 'react';
import { useRouter } from "next/router";
import { Form , Input, Button } from 'antd';
import useSWR from 'swr';
import { isEmpty } from "lodash";
import { login } from '../lib/api'
import { useAuth } from "../lib/hooks";
import styles from '../styles/Login.module.css';


// TODO: Handle the display of error on notification
const Login = () => {
  const router = useRouter();
  const { auth, setAuth } = useAuth();

  if (auth?.access) {
    router.push("/dashboard");
  }

  const [payload, setPayload] = useState({})
  const onFinish = ({email, password}) => { setPayload({ email, password}); };
  const onSuccessHandler = (data) => {
    setAuth(auth =>({...auth, ...data}));
    setPayload({});
  };
  useSWR(!isEmpty(payload) ? payload : null, login, {
    onSuccess: onSuccessHandler,
    onError: (error) => setPayload({}),
    shouldRetryOnError: false,
  });

  return (
    <Form
      name="basic"
      labelCol={{ span: 8 }}
      wrapperCol={{ span: 16 }}
      initialValues={{ remember: true }}
      onFinish={onFinish}
      autoComplete="off"
    >
      <Form.Item
        name="email"
        rules={[{ required: true, message: 'Please input your email!' }]}
      >
        <Input placeholder={"Email"}/>
      </Form.Item>

      <Form.Item
        name="password"
        rules={[{ required: true, message: 'Please input your password!' }]}
      >
        <Input.Password placeholder={"Password"}/>
      </Form.Item>

      <Form.Item wrapperCol={{ offset: 8, span: 16 }}>
        <Button type="primary" htmlType="submit">
          Submit
        </Button>
      </Form.Item>
    </Form>
  );
};

export default Login;