import type {IBaseDjangoProps} from "@/types/base";

interface IHelloProps extends IBaseDjangoProps {
  msg: string
}

interface INewComponentProps extends IBaseDjangoProps {
    hello: string
}

export type { IHelloProps, INewComponentProps }